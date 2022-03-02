from django.db import models

# Create your models here.

class Advt(models.Model):
    advt_dt = models.DateTimeField(auto_now=True)
    advt_name = models.CharField(max_length=200, verbose_name='Advertisement name')
    advt_img = models.ImageField(upload_to='adver/')
    advt_price = models.CharField(max_length=100, verbose_name='Price')
    advt_link = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.advt_name

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"