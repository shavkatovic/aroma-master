from django.db import models


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
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    message = models.TextField()
