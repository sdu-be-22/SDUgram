from django.shortcuts import render, redirect
from .forms import UserAuthenticationForm
from django.contrib.auth import authenticate, login as log, logout
from django.contrib import messages
# Create your views here.
def login(request):

    if request.method == 'POST':
        form = UserAuthenticationForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log(request, user)
            messages.success(request, f'Successfuly authorized!')
            redirect('Home')
        else:
            messages.warning(request, f'Incorect password or username!')
    else:
        form = UserAuthenticationForm()
    # if request.method == 'POST':
    #     form = UserAuthenticationForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         #success_url = reverse_lazy('login')
    #         return redirect('Home')
        # else:
        #     messages.warning(request, f' Please enter the valid info! ')
        #     return redirect('register')
    # else:
    #     form = UserAuthenticationForm()
    return render(request, 'signIN/login.html', {'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')
