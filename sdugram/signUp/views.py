from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account is successfully created for {user.username}!')
            login(request, user)
            return redirect('Home')
        else:
            username = request.POST["username"]
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.warning(request, f'Account with {username} username is already created: Please LOG IN!')
                return redirect('login')
            else:
                messages.warning(request, f'Please fill the register form properly!')
                return redirect('register')

    else:
        form = UserRegisterForm()
        return render(request, 'signUp/register.html', {'form': form})