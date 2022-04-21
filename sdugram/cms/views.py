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

    #favorite_posts = Advt.objects.all()
    favorite_posts = request.user.profile.fav_adver.all()
    print(favorite_posts)
    print(Advt.objects.all())
    context={
        'favorite_posts':favorite_posts,
    }
    # if request.GET.get('favbtn'):
    #     fpost=favorite_posts.get(advt_host_id=id)
    #     fpost.advertisement_favourites == 1
    #     fpost.save()

    return render(request, 'favorites.html',context)

def add_fav(request, id):
    temp = get_object_or_404(Advt, pk=id)

    if temp.advertisement_favourites == 1:
        temp.advertisement_favourites = 0
    else:
        temp.advertisement_favourites ==1
    temp.save()
    return redirect('Home')




def favorite_post(request,id):
    post=get_object_or_404(CmsSlider,id=id)
    if post.favorite.filter(id=request.user.id).exists():
        post.favorite.remove(request.user)
    else:
        post.favorite.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())

def count_posts(request):
    services=Advt.objects.filter(advertisement_category=1).count()
    job = Advt.objects.filter(advertisement_category=2).count()
    transport =  Advt.objects.filter(advertisement_category=3).count()
    real_estate =  Advt.objects.filter(advertisement_category=4).count()
    fashion= Advt.objects.filter(advertisement_category=5).count()
    animals= Advt.objects.filter(advertisement_category=6).count()
    electronics= Advt.objects.filter(advertisement_category=7).count()
    childworld= Advt.objects.filter(advertisement_category=8).count()
    giveaways = Advt.objects.filter(advertisement_category=9).count()
    houseandgarden= Advt.objects.filter(advertisement_category=10).count()
    sports= Advt.objects.filter(advertisement_category=11).count()

    ers={'services':services,
        'job':job,
        'transport':transport,
        'real_estate':real_estate,
        'fashion':fashion,
        'animals':animals,
        'electronics':electronics,
        'childworld':childworld,
        'giveaways':giveaways,
        'houseandgarden':houseandgarden,
        'sports':sports }

    return render(request,'category_info.html',ers)