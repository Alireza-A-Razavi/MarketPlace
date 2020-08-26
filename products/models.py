from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils.translation import ugettext_lazy as _

from .custom_fields import IntegerRangeField
from users.models import ProducerProfile, Profile, User
from categories.models import Category

########################################################################################
"""
Notes:
1- adding tinymce for description
2- Creating the category model in the databasse
"""
########################################################################################
class Product(models.Model):
    SAMPLE_CHOICES = (
        ("خیر","خیر"),
        ("رایگان","رایگان"),
        ("اعمال هزینه","اعمال هزینه"),
    )
    title = models.CharField(max_length=132, verbose_name='نام محصول')
    producer = models.ForeignKey(ProducerProfile, on_delete=models.CASCADE)
    price = models.FloatField(blank=True, null=True, verbose_name="قیمت محصول")
    category = models.ManyToManyField(Category)
    discount_price = models.FloatField(blank=True, null=True, verbose_name="قیمت تخفیف")
    product_image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    stock = models.IntegerField(default=1, verbose_name='موجودی')
    description = models.TextField() #tiny-mce will be added  on the next run
    minimum_order = models.CharField(max_length=32, verbose_name='حداقل تعداد جهت سفارش', null=True, blank=True)
    payment_type = models.CharField(max_length=32, verbose_name='روش پرداخت', null=True, blank=True)
    packing = models.CharField(max_length=32, verbose_name="بسته بندی", null=True, blank=True)
    shipping = models.CharField(max_length=32, verbose_name="نحوه ارسال", null=True, blank=True)
    origin = models.CharField(max_length=32, verbose_name="اصالت کالا", null=True, blank=True)
    made_in = models.CharField(max_length=32, verbose_name="تولید کشور", null=True, blank=True)
    delivery = models.CharField(max_length=32, verbose_name="بازه زمانی ارسال", null=True, blank=True)
    samples = models.CharField(max_length=24, verbose_name="ارائه نمونه", null=True,
                                blank=True, choices=SAMPLE_CHOICES)
    remarks = models.TextField(verbose_name="ملاحظات", null=True, blank=True)


    def __str__(self):
        return f"{self.title} by {self.producer.company_name}"

    def save(self, *args, **kwargs):
        slug_1 = slugify(self.title)
        qs = Product.objects.filter(slug=self.title)
        exists = qs.exists()
        if exists:
            new_slug = "%s-%s" % (slug_1, self.id)
            self.slug = new_slug
        else:
            self.slug = slug_1
        super(Product, self).save(*args, **kwargs)


    def average_rating(self):
        sum = 0
        ratings = Rating.objects.filter(product=self)
        for rating in ratings:
            sum = sum + rating.stars
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0

    def get_comments(self):
        comments = ProductComment.objects.filter(product=self, is_confirmed=True)
        return comments


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # size

    class Meta:
        unique_together = (
            ('product', 'name')
        )

    def __str__(self):
        return self.name


class ProductVariation(models.Model):
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)  # S, M, L
    attachment = models.ImageField(blank=True)

    class Meta:
        unique_together = (
            ('variation', 'value')
        )

    def __str__(self):
        return self.value


class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    is_confirmed = models.BooleanField(default=False)
    content = models.TextField(verbose_name="متن نظر")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")

    def __str__(self):
        return f"{self.user.username} comment for {self.product.title}"

class Rating(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  stars = IntegerRangeField(min_value=1, max_value=5, verbose_name="امتیاز")

  class Meta:
    unique_together = (('user', 'product'),)
    index_together = (('user', 'product'),)
