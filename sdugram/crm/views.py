from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telegrambot.sendMessage import sendTelegram
from grid_panel.models import Advt


# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    advt_list = Advt.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()

    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table,
                'form': form,
                'advt_list': advt_list}
    return render(request, './index.html', dict_obj)


def Adboard(request):
    advt_list = Advt.objects.all()
    dict_obj = {'advt_list': advt_list}
    return render(request, './grid.html', dict_obj)


def thanks_page(request):
    form = OrderForm(request.POST, request.FILES)
    # img = request.POST['img']
    if form.is_valid():
        form.save()
        # Get the current instance object to display in the template
    name = request.POST['name']
    phone = request.POST['phone']

    # element = Order(order_name = name, order_phone = phone)
    # element.save()
    # img = 'order_img/' + img;
    sendTelegram(tg_name=name, tg_phone=phone)

    return render(request, './thanks.html', {'name': name,
                                             'phone': phone}
                  )
