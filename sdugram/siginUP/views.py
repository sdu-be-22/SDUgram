from django.shortcuts import render, redirect
from .models import Account, UserInformation
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def signUPForm(request):
    return render(request, 'signUp.html')


def submission(request):
    if request.POST["password1"] != request.POST["password2"]:
        return render(request, 'signUp.html', {'invalidPassword': True})
    elif not Account.objects.filter(email=request.POST["email"]).exists():
        return render(request, 'signUp.html', {'invalidEmail': True})
    else:  """If there is no errors in registration"""
    newAccount = Account()
    newAccount.email = request.POST["email"]
    newAccount.password = request.POST["password1"]
    # newAccount.information = UserInformation()
    # newAccount.information.save()
    # newAccount.save()
    subject = "Heeey! Welcome to SDUgram website!!!"
    message = 'We are glad to see you in our site. Here you can find everything you need and look for, also you can give to your things the second life for reusing! Good luck in using!'
    sender = settings.EMAIL_HOST_USER
    send_mail(subject, message, sender, [request.POST["email"]], fail_silently=False)
    return render(request, "signUp.html", {'messageIsSent':True})





