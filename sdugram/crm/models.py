from django.db import models

# Create your models here.
class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Status name')
    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='First name')
    order_phone = models.CharField(max_length=200, verbose_name='phone ')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Status')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

class CommentCrm(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Zayavka')
    coment_text = models.TextField(verbose_name='Text commentary')
    coment_dt = models.DateTimeField(auto_now=True, verbose_name='Date created')

    def __str__(self):
        return self.coment_text

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentaries"



