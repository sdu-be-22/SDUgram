from django.shortcuts import render, redirect
# from .models import Favorites
from grid_panel.models import Advt
from django.contrib import messages

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
    favorite_posts = request.user.profile.fav_adver.all()
    context={
        'favorite_posts':favorite_posts,
    }
    # if request.GET.get('favbtn'):
    #     fpost=favorite_posts.get(advt_host_id=id)
    #     fpost.advertisement_favourites == 1
    #     fpost.save()

    return render(request, 'favorites.html',context)