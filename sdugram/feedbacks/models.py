from django.db import models

# Create your models here.
class FeedbackModel(models.Model):
    name = models.CharField(max_length=40, default="")
    description = models.CharField(max_length=10_000, default="")
    username = models.CharField(max_length=32, default="Guest")
    like = models.IntegerField(default=0)
    