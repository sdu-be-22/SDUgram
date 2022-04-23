from django.contrib import admin
from .models import Advt, Category
# Register your models here.

class AdvtAdmin(admin.ModelAdmin):
    prepopulated_fields = {'advertisement_slug': ('advertisement_name',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Advt, AdvtAdmin)
admin.site.register(Category, CategoryAdmin)