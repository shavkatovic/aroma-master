from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import Product, Category, Blog, BlogImages, BlogCategory

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(BlogCategory)


class BlogImageInline(TabularInline):
    model = BlogImages
    fields = 'image',
    extra = 1



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline]
