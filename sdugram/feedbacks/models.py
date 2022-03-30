from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class FeedbackModel(models.Model):
    name = models.CharField(max_length=40, default="")
    caption = models.TextField(default="Empty")
    date_posted = models.DateTimeField(default = timezone.now)
    like = models.IntegerField(default=0)

    