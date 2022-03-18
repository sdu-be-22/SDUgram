from django.db import models

# Create your models here.
class Account(models.Model):
    email = models.EmailField(max_length=65, null=True)
    password = models.CharField(max_length=150, null=True)
    firstName = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    gender = [('M','Male'),
              ('F','Female')]
    phone = models.CharField(max_length=12, null=True)
    city = models.CharField(max_length=40, null=True)
    photo = models.ImageField(null=True)

    def __str__(self):
        return self.firstName,self.lastName
