from django.contrib import admin
from .models import Account, UserInformation
# Register your models here.
admin.site.register(Account)
admin.site.register(UserInformation)