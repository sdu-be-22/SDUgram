from django.contrib import admin
from .models import Advt, Category
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Advt)
admin.site.register(Category, CategoryAdmin)