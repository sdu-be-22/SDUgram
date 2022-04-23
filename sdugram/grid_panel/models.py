from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Advt(models.Model):
    advertisement_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    advertisement_date_created = models.DateField(auto_now=True,)
    advertisement_name = models.CharField(max_length=200, verbose_name='Advertisement name')
    advertisement_image = models.ImageField(upload_to='media/adver/', null=True)
    advertisement_price = models.IntegerField(verbose_name='Price', null=True)
    advertisement_description = models.TextField(max_length=1000, default="")
    advertisement_favourites = models.IntegerField(default=0)
    advertisement_location = models.CharField(max_length=30, default="Алматы")
    advertisement_category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='category')
    advertisement_view = models.IntegerField(default=0)
    advertisement_slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.advertisement_name

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"

    def get_absolute_url(self):
        return reverse('adver', kwargs={'adver_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='static/img/category', null=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
