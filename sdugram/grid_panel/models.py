from django.db import models


# Create your models here.
from django.urls import reverse


class Advt(models.Model):
    advt_host_id = models.IntegerField(default=1)
    advt_item_id = models.IntegerField(default=-1)
    advt_date_created = models.DateField(auto_now=True)
    advt_type = models.CharField(max_length=100, default="Другие")
    advt_dt = models.DateTimeField(auto_now=True)
    advt_name = models.CharField(max_length=200, verbose_name='Advertisement name')
    advt_img = models.ImageField(upload_to='adver/')
    advt_price = models.CharField(max_length=100, verbose_name='Price')
    advt_link = models.CharField(max_length=200, null=True)
    advt_description = models.CharField(max_length=1000, default="")
    advt_favourite = models.IntegerField(default=0)
    advt_views = models.IntegerField(default=0)
    advt_location = models.CharField(max_length=30, default="Алматы")
    advt_cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.advt_name

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"

    def get_absolute_url(self):
        return reverse('adver', kwargs={'adver_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
