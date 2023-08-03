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


class Comment(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    message = models.TextField()
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='product')


class BlogCategory(models.Model):
    title = models.CharField(max_length=128)


class Blog(models.Model):
    image = models.ImageField(upload_to='blog/image')
    title = models.CharField(max_length=128)
    descriptions = models.TextField(blank=True, null=True)
    category = models.ManyToManyField('products.BlogCategory', related_name='blog')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
