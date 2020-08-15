from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.shortcuts import reverse

GENDER_CHOICE = (
    ('خانم','خانم'),
    ('آقای','آقای'),
)

class User(AbstractUser):
    is_producer = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    #pk is passed
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = User.first_name
    last_name = User.last_name
    gender = models.CharField(max_length=17, choices=GENDER_CHOICE, verbose_name="جنسیت")
    province = models.CharField(max_length=132, blank=True, null=True, verbose_name="استان")
    city = models.CharField(max_length=132, blank=True, null=True, verbose_name="شهر")
    company_name = models.CharField(max_length=132, blank=True, null=True, verbose_name="نام شرکت")
    company_address = models.TextField(blank=True, null=True, verbose_name='آدرس کارخانه یا شرکت')
    office_address = models.TextField(blank=True, null=True, verbose_name='آدرس دفتر')
    intoduce_yourself = models.TextField(blank=True, null=True, verbose_name='معرفی مختصر شرکت')
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    
    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse('users:my_profile', kwargs={'pk': self.pk})


class ProducerProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = User.first_name
    last_name = User.last_name
    gender = models.CharField(max_length=17, choices=GENDER_CHOICE, verbose_name="جنسیت")
    province = models.CharField(max_length=132, blank=True, null=True, verbose_name="استان")
    city = models.CharField(max_length=132, blank=True, null=True, verbose_name="شهر")
    company_name = models.CharField(max_length=132, blank=True, null=True, verbose_name="نام شرکت")
    company_address = models.TextField(blank=True, null=True, verbose_name='آدرس کارخانه یا شرکت')
    office_address = models.TextField(blank=True, null=True, verbose_name='آدرس دفتر')
    intoduce_yourself = models.TextField(blank=True, null=True, verbose_name='معرفی مختصر شرکت')
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")


    def __str__(self):
        return self.user.username

