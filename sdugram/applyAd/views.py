from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from telegrambot.sendMessage import sendTelegram
from grid_panel import *
from myProfile.models import *
import telebot


# Create your views here.
def image_view(request):
    if request.method == 'POST':
        form = AdApplicationForm(request.POST or None, request.FILES, instance=request.user)

        if form.is_valid():
            user = form.save()
            # return redirect('success')
            messages.success(request, f'Your advertisement is successfully uploaded!{user.username}')
            return redirect('Home')

    else:
        form = AdApplicationForm(instance=request.user)
    return render(request, 'applyAd/image_app.html', {'form': form})


def success(request):
    if request.method == 'GET':
        Ads = Advt.objects.all()
        size = len(Ads)
        Ads = Advt.objects.get(pk=size)
        profile =Profile.objects.get(user=request.user)
        sendTelegram(tg_name=Ads.advertisement_name, tg_phone=profile.phone,tg_desc=Ads.advertisement_description, tg_location=Ads.advertisement_location, tg_img=Ads.advertisement_image)

    # element = Order(order_name = name, order_phone = phone)
    # element.save()
    # img = 'order_img/' + img;
    return render(request, 'thanks.html', {'ads': Ads})
   # return HttpResponse('Successfully uploaded to Moderation')

