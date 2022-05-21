from django.db import models

# Create your models here.

class Questions(models.Model):
    q_name = models.CharField(max_length=55, verbose_name="Question")
    q_ans = models.CharField(max_length=3000, verbose_name='Answer')
    class Meta:
        verbose_name = "question"
        verbose_name_plural = "Questions"
        ordering = ['q_name',]