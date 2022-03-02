from django.shortcuts import render
from .models import SignUpModel
# Create your views here.
def signUPForm(request):
    return render(request, './signUp.html')

def submission(request):
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    account = SignUpModel(first_name = firstName, last_name = lastName)
    account.save()
    return render(request, './submission.html', {'account':account})