from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','phone', 'gender', 'address', 'avatar')
    search_fields = ('user','address')
    list_filter = ('gender', 'address')
    list_editable = ('phone',)
admin.site.register(Profile, ProfileAdmin)
