from django.shortcuts import render, redirect

# Create your views here.
from .models import Favorites
from grid_panel.models import Advt


def add_favorite(request, advt):
    data = {'success': False}
    advt_obj = Advt.objects.get(pk = advt)
    if advt_obj in request.user.profile.fav_adver.all():
        request.user.profile.fav_adver.remove(advt_obj)
    else:
        request.user.profile.fav_adver.add(advt_obj)
    data['success'] = True

    return redirect('Home')