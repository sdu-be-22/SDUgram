from django import forms
from .models import Order


class OrderForm(forms.Form):

    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    img = forms.ImageField()

    class Meta:
        model = Order
        fields = ('title', 'image')