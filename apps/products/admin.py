from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import Product, Category, Blog, BlogCategory

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(BlogCategory)
