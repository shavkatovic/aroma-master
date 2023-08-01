from django.db import models


# Create your models here.


class Comments(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    rate = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

