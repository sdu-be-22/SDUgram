from django.contrib import admin
from .models import Messages
# Register your models here.
admin.site.site_header = 'SDUGRAM admin panel'
class MessagesAdmin(admin.ModelAdmin):
    exclude = ('date',) # --fields to exclude in the detail view
    list_display = ('subject', 'date', 'from_user', 'to_user')
    list_filter = ('date','from_user')
    search_fields = ('subject',)
admin.site.register(Messages, MessagesAdmin)
