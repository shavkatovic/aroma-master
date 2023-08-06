from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import Product, Category, Blog, BlogCategory, BlogImages

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
# admin.site.register(Blog)
admin.site.register(BlogCategory)


class BlogImagesadmin(TabularInline):
    model = BlogImages
    fields = 'image',
    extra = 1


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = 'title',
    inlines = [BlogImagesadmin]
