from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserAuthenticationForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']
