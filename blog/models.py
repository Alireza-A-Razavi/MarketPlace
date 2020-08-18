from django.db import models
from tinymce.models import HTMLField
from categories.models import Category
from users.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.encoding import python_2_unicode_compatible
from hitcount.models import HitCount, HitCountMixin
from django.template.defaultfilters import slugify
from django.shortcuts import reverse


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=1024, verbose_name="نام پست")
    short_description = models.TextField(verbose_name="توضیح پیش نمایش")
    content = HTMLField(verbose_name="متن پست")
    timestamp = models.DateField(auto_now=True, verbose_name="تاریخ ثبت دست")
    thumbnail = models.ImageField(verbose_name="تصویر پست")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="دسته بندی")
    featured = models.BooleanField(default=False)
    active_post = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field="object_pk"
                                        ,related_query_name="hit_count_generic_relation")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('post-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'slug': self.slug})

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    @property
    def get_comment(self):
        return self.comments.all().order_by('-timestamp')



