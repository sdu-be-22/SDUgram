from django.db import models

# Create your models here.


class Ad(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=2000, null=True)
    location = models.CharField(max_length=200, null=True)
    ad_img = models.ImageField(upload_to='order_img/')

