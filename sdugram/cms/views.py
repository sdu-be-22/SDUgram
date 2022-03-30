from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import CmsSlider
from grid_panel.models import Advt

def post_detail(request, id):
    post = get_object_or_404(CmsSlider, pk=id)
    is_favorite = False
    if post.favorite.filter(id=request.user.id).exists():
        is_favorite = True

    context = {
        'post':post,
        'is_favorite':is_favorite,
    }

    return render(request,'grid.html',context)

def post_favorite_list(request):
    #user = request.user
    favorite_posts = Advt.objects.all()
    context={
        'favorite_posts':favorite_posts,

    }
    if request.GET.get('favbtn'):
        fpost=favorite_posts.get(advt_host_id=id)
        fpost.advt_favourite == 1
        print("SSSS")
        fpost.save()

    return render(request, 'favorites.html',context)

def add_fav(request, id):
    temp = get_object_or_404(Advt, pk=id)
    print('Debug')
    print(temp.advt_favourite)
    if temp.advt_favourite == 1:
        temp.advt_favourite = 0
    else:
        temp.advt_favourite = 1
    temp.save()
    return redirect('Home')




def favorite_post(request,id):
    post=get_object_or_404(CmsSlider,id=id)
    if post.favorite.filter(id=request.user.id).exists():
        post.favorite.remove(request.user)
    else:
        post.favorite.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())