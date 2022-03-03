from django.db import models


# Create your models here.
class Account(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = [('M','Male'),
              ('F','Female')]
    email = models.EmailField(max_length=65)
    phone = models.CharField(max_length=12)
    city = models.CharField(max_length=40)
    photo = models.ImageField(null = True)
    status = models.CharField(max_length=10, default="False")

    def __str__(self):
        return self.firstName + ' ' + self.lastName