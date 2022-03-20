from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account is successfully created for {username}!')
            login(request, user)
            return redirect('Home') # will add 'Home' redirect
        # else:
        #     messages.warning(request, f' Please enter the valid info! ')
        #     return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'signUp/register.html', {'form':form})