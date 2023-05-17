from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    user_age = models.IntegerField(blank=False, null=True)
    user_city = models.CharField(max_length=30, blank=False, null=True)
    user_phone = PhoneNumberField(region='PK')
    user_address = models.TextField(blank=False, null=True)
    user_freelancer = models.BooleanField(default=False,blank=True, null=True)
    user_bio = models.TextField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='image/%y', blank=True, default=None)
    user_website = models.URLField(blank=False, null=False)

