from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def main_page(request):
    return render(request, 'myProfile.html')
@login_required
def updateProfile(request):
    if request.method == 'POST':

        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if request.POST.get('reset'):
            request.user.first_name = ''
            request.user.last_name = ''
            Profile.objects.get(user=request.user).delete()
            Profile.objects.create(user=request.user)
            request.user.save()
            messages.warning(request, 'Warning! All information in profile is dropped!')
            return redirect('myProfile')
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('myProfile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'updateUser.html', {'user_form': user_form, 'profile_form': profile_form})