from django import forms
from .models import *

class AdForm(forms.ModelForm):
    # name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Ad
        fields = ['name', 'phone', 'description', 'location', 'ad_img']