from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class FeedbackModel(models.Model):
    user = models.CharField(max_length=40, default="Guest")
    name = models.CharField(max_length=40, default="")
    caption = models.TextField(default="Empty")
    date_posted = models.DateTimeField(default = timezone.now)
    like = models.IntegerField(default=0)

class FeedbackItemModel(models.Model):
    user = models.CharField(max_length=40, default="Guest")
    caption = models.TextField(default="Empty")
    date_posted = models.DateTimeField(default = timezone.now)
    item = models.IntegerField(default=-1)
    
    