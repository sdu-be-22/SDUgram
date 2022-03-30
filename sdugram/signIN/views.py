from django.shortcuts import render, redirect
from .forms import UserAuthenticationForm
from django.contrib.auth import authenticate, login as log, logout
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log(request, user)
            messages.success(request, f'Welcome {username}! You are successfully logged in!')
            return redirect('Home')
        else:
            messages.warning(request, 'Incorrect password or username!')
            return redirect('login')
    else:
        form = UserAuthenticationForm()
    return render(request, 'signIN/login.html', {'form':form})

def logout_user(request):
    logout(request)
    return redirect('Home')
