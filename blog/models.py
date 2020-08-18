from django.db import models
from tinymce.models import HTMLField
from RLBlog.categories.models import Category
from RLBlog.users.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.encoding import python_2_unicode_compatible
from hitcount.models import HitCount, HitCountMixin

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=1024, verbose_name="نام پست")
    short_description = models.TextField(verbose_name="توضیح پیش نمایش")
    content = HTMLField(verbose_name="متن پست")
    timestamp = models.DateField(auto_now=True, verbose_name="تاریخ ثبت دست")
    thumbnail = models.ImageField(verbose_name="تصویر پست")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="دسته بندی")
    featured = models.BooleanField(default=False)
    active_post = models.BooleanField(default=True)
    slug = models.SlugField()
    hit_count_generic = GenericRelation(HitCount, object_id_field="object_pk"
                                        ,related_query_name="hit_count_generic_relation")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
