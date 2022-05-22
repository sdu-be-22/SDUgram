from django.contrib import admin
from .models import Advt, Category
# Register your models here.
class AdvtAdmin(admin.ModelAdmin):
    exclude = ('advertisement_view','advertisement_favourites')
    list_display = ('advertisement_name', 'advertisement_date_created', 'advertisement_user')
    list_filter = ('advertisement_date_created', 'advertisement_user')
    list_editable = ('advertisement_user',)
    search_fields = ('advertisement_name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    list_editable = ('image',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Advt, AdvtAdmin)
admin.site.register(Category, CategoryAdmin)