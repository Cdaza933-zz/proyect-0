from django.db import models


# Create your models here.
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=False, blank=False,on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=False, blank=False)
    place = models.CharField(max_length=255, null=False, blank=False)
    beginning_date = models.DateTimeField(null=False,blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    host = models.ForeignKey(User, null=False, blank=False,on_delete=models.CASCADE)
    image = models.CharField(max_length=255, null=True)
