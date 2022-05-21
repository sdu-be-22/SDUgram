from django.contrib import admin
from .models import Questions
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('q_name','q_ans')
    search_fields = ('q_name',)

admin.site.register(Questions, QuestionAdmin)
