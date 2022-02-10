from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    text = 'new Text'
    a = 'hello world'
    return render(request, './index.html', {
        'a': a,
        'text':text
    })
