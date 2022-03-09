from django.db import models


# Create your models here.
class UserInformation(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = [('M','Male'),
              ('F','Female')]
    phone = models.CharField(max_length=12)
    city = models.CharField(max_length=40)
    photo = models.ImageField(null = True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Account(models.Model):
    email = models.EmailField(max_length=65)
    password = models.CharField(max_length=150)
    information = models.ForeignKey(UserInformation, on_delete=models.CASCADE, null=True)
