from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils.translation import ugettext_lazy as _


from users.models import ProducerProfile, Profile, User
# from categories.models import Category

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
    # category = models.ManyToManyField(Category)
    discount_price = models.FloatField(blank=True, null=True, verbose_name="قیمت تخفیف")
    product_image = models.ImageField(null=True, blank=True)
    slug = models.SlugField()
    stock = models.IntegerField(default=1, verbose_name='موجودی')
    discription = models.TextField() #tiny-mce will be added  on the next run
    minumum_order = models.CharField(max_length=32, verbose_name='حداقل تعداد جهت سفارش', null=True, blank=True)
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
