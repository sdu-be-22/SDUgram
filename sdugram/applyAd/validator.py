from django import forms
from django.contrib import messages
from django.core.files.images import get_image_dimensions
from django.shortcuts import redirect


def validate_image(self, request):
    image = self.cleaned_data.get('advertisement_image')
    if not image:
        return False
    else:
        w, h = get_image_dimensions(image)
        if w > 500:
            # raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 500px" % w)
            messages.warning(request, "The image is %i pixel wide. It's supposed to be 500px" % w)
            return redirect('apply')
        if h > 500:
            # raise forms.ValidationError("The image is %i pixel high. It's supposed to be 200px" % h)
            messages.warning(request, "The image is %i pixel high. It's supposed to be 200px" % h)
            return redirect('apply')
    return image
