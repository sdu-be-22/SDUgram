from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(max_length=13, null=True)
    gender = models.CharField(choices=gender_choices, max_length=7, default='Male')
    instagram_account = models.CharField(blank=True, max_length=50)
    avatar = models.ImageField(blank = True, default='profile_images/default_avatar.png', upload_to='profile_images')
