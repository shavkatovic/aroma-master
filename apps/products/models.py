from django.db import models
from django.db.models import ForeignKey, ImageField, CASCADE


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=128)

    class Meta:
        db_table = 'category'


class Product(models.Model):
    image = models.ImageField(upload_to='product/image')
    name = models.CharField(max_length=128)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    category = models.ManyToManyField('products.Category', 'product')
    descriptions = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()


# {% if product.quantity %}In stock {% else %} Out of
#                                 Stock{% endif %}


class Post(models.Model):
    class Position(models.IntegerChoices):
        one = 1, '1'
        two = 2, '2'
        three = 3, '3'
        four = 4, '4'
        five = 5, '5'

    positions = models.IntegerField(choices=Position.choices, default=Position.three, verbose_name=Position)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    message = models.TextField()
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='product')


class BlogCategory(models.Model):
    title = models.CharField(max_length=128)


class Blog(models.Model):
    title = models.CharField(max_length=128)
    descriptions = models.TextField(blank=True, null=True)
    category = models.ManyToManyField('products.BlogCategory', related_name='blog')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)


class BlogImages(models.Model):
    blog = ForeignKey('products.Blog', CASCADE, 'images')
    image = ImageField(upload_to='images/blog/')
