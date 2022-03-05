from django import forms
from .models import *

class AdForm(forms.ModelForm):
    # name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # img = forms.ImageField()

    class Meta:
        model = Ad
        fields = ['name', 'phone','ad_img']