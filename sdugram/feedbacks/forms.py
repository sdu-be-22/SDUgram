from django import forms

class FeedbackForm(forms.Form):
    title = forms.CharField(max_length=32, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)   

class FeedBackItemForm(forms.Form):
    Comments = forms.CharField(widget=forms.Textarea(attrs={'style': 'width=300px;','class': 'form-control'}), required=True)
