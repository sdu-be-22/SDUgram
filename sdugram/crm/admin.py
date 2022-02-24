from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm

# Register your models here.
admin.site.register(Order)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)