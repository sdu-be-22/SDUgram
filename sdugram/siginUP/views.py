from django.shortcuts import render
from .models import Account
# Create your views here.
def signUPForm(request):
    return render(request, 'signUp.html')

def submission(request):
    newAccount = Account()
    if Account.objects.filter(email=request.POST['email']).exists:
        error_message = "Account with this email already exists. Please use another email!"
    if int(request.POST['age'])<18:
        age_error = "Age is not sufficient!"
    else:
        newAccount.firstName = request.POST['firstName']
        newAccount.lastName = request.POST['lastName']
        newAccount.city = request.POST['city']
        newAccount.age = request.POST['age']
        newAccount.gender = request.POST['gender']
        newAccount.phone = request.POST['phone']
        newAccount.email = request.POST['email']
        newAccount.save()
    return render(request, './submission.html', {'account': newAccount, 'error_message':error_message,'age_error':age_error})
