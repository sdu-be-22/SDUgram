from django import forms
from .models import *
from chat.models import *

class MessageForm(forms.ModelForm):


    class Meta:
        model = Messages
        fields = ['to_user', 'subject', 'message']
