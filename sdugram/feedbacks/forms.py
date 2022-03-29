from django import forms

class FeedbackForm(forms.Form):
    title = forms.CharField(max_length=32, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)   
