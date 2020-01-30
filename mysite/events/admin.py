from django.contrib import admin

# Register your models here.
from events.models import Category

admin.site.register(Category)