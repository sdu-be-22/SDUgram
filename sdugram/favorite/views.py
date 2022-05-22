from inspect import Attribute
from django.shortcuts import render, redirect
# from .models import Favorites
from grid_panel.models import Advt
from django.contrib import messages
from signIN.forms import UserAuthenticationForm
from django.contrib.auth import authenticate, login as log, logout

def add_favorite(request):
    data = {'success': False}
    if request.method == "POST":
        val = request.POST.get('id')
        advt_obj = Advt.objects.get(pk=val)
        if advt_obj in request.user.profile.fav_adver.all():
            request.user.profile.fav_adver.remove(advt_obj)
        else:
            request.user.profile.fav_adver.add(advt_obj)
        data['success'] = True

    return redirect('Home')

def post_favorite_list(request):
    #user = request.user

    #favorite_posts = Advt.objects.all()
    try:
        favorite_posts = request.user.profile.fav_adver.all()
        context={
            'favorite_posts':favorite_posts,
        }
        # if request.GET.get('favbtn'):
        #     fpost=favorite_posts.get(advt_host_id=id)
        #     fpost.advertisement_favourites == 1
        #     fpost.save()
        return render(request, 'favorites.html',context)
    except AttributeError:
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
