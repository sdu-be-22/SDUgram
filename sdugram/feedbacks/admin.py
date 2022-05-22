from django.contrib import admin

from .models import FeedbackItemModel, FeedbackModel
# Register your models here.
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'name','caption', 'date_posted')
    list_filter = ('user', 'date_posted')
    search_fields = ('name','caption')
# class FeedbackItemModel(admin.ModelAdmin):
#     list_display = ()
admin.site.register(FeedbackModel, FeedbackModelAdmin)
admin.site.register(FeedbackItemModel)