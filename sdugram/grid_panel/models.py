from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Advt(models.Model):
    advertisement_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='User')
    advertisement_date_created = models.DateField(auto_now=True,verbose_name='Date created')
    advertisement_name = models.CharField(max_length=200, verbose_name='Name')
    advertisement_image = models.ImageField(upload_to='media/adver/', null=True, verbose_name='Image')
    advertisement_price = models.IntegerField(verbose_name='Price', null=True,)
    advertisement_description = models.TextField(max_length=1000, default="", verbose_name='Description')
    advertisement_favourites = models.IntegerField(default=0, verbose_name='Favourites')
    advertisement_location = models.CharField(max_length=30, default="Алматы", verbose_name='Location')
    advertisement_category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')
    advertisement_view = models.IntegerField(default=0)

    def __str__(self):
        return self.advertisement_name

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"
        ordering = ['-advertisement_date_created',]

    def get_absolute_url(self):
        return reverse('adver', kwargs={'adver_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Category name")
    image = models.ImageField(upload_to='static/img/category', null=True, verbose_name='Image')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['-pk',]
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
