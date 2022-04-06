from django.contrib import admin

from .models import FeedbackItemModel, FeedbackModel
# Register your models here.
admin.site.register(FeedbackModel)
admin.site.register(FeedbackItemModel)