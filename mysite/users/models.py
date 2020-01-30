from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    date_updated = models.DateTimeField(null=False, auto_now=True)
    date_created = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
