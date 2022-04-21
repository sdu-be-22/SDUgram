from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from grid_panel.models import *
from .forms import *
from applyAd.forms import *

# Create your views here.
def show_my_advertisements(request):
    advertisements = Advt.objects.filter(advertisement_user=request.user)
    return render(request, 'MyAdvertisements.html', {'advt_list': advertisements})
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
def editAdver(request, adver_id):
    adver = Advt.objects.get(pk=adver_id)
    if request.method == "POST":
        edit_adver = AdApplicationForm(request.POST, request.FILES, instance=adver)
        if edit_adver.is_valid():
            edit_adver.save()
            messages.success(request, f'Advertisement {adver.advertisement_name} is updated!')
            return redirect('myAdvertisements')
    elif request.GET.get('remove'):
        adver.delete()
        return redirect('myAdvertisements')
    else:
        advForm = AdApplicationForm(instance=adver)
        return render(request, 'editAdver.html',{'form':advForm})


