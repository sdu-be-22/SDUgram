from django import forms
from django.contrib import messages
from django.core.files.images import get_image_dimensions
from django.shortcuts import redirect

from .models import *
from grid_panel.models import *


class AdApplicationForm(forms.ModelForm):
    class Meta:
        model = Advt
        fields = ['advertisement_name', 'advertisement_description', 'advertisement_price', 'advertisement_location',
                  'advertisement_category', 'advertisement_image']
