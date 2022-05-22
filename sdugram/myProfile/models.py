from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
from grid_panel.models import Advt
class Profile(models.Model):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=13)
    gender = models.CharField(blank=True, choices=gender_choices, max_length=7)
    instagram_account = models.CharField(blank=True, max_length=50)
    avatar = models.ImageField(blank=True, default='profile_images/default_avatar.png', upload_to='media/profile_images/')
    fav_adver = models.ManyToManyField(Advt)

    class Meta:
        verbose_name_plural = 'Profiles'
        verbose_name = 'profile'

def save(self, *args, **kwargs):
    super().save()

    img = Image.open(self.avatar.path)

    if img.height > 100 or img.width > 100:
        new_img = (100, 100)
        img.thumbnail(new_img)
        img.save(self.avatar.path)