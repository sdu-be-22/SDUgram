from django.db import models

# Create your models here.

class Questions(models.Model):
    q_name = models.CharField(max_length=55)
    q_ans = models.CharField(max_length=3000)