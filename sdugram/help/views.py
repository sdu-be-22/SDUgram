from django.shortcuts import render
from help.models import Questions
# Create your views here.

def help_page(request):
    q_list = Questions.objects.all()
    return render(request, './help.html', {'q_list': q_list})
