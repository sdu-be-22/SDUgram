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
            # p1 = request.POST['password1']
            # p2 = request.POST['password2']
            # messages.warning(request, f' Please fill the register form properly! {form.error_messages.__str__()}, {p1} {p2}')
            # return redirect('register')
            username = request.POST["username"]
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.warning(request, f'Account with {username} username is already created: Please LOG IN!')
                return redirect('login')
            else:
                messages.warning(request, f'Please fill the register form properly! {form.error_messages.values().__str__()}')
                return redirect('login')

    else:
        form = UserRegisterForm()
        return render(request, 'signUp/register.html', {'form': form})