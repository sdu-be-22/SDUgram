from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import OrderForm
from telegrambot.sendMessage import sendTelegram
from grid_panel.models import Advt


# Create your views here.
def first_page(request):
    advt_list = Advt.objects.all()
    dict_obj = {'advt_list': advt_list}
    return render(request, './index.html', dict_obj)


def advt_detail_view(request):
    advt_list = Advt.objects.all()
    paginator = Paginator(advt_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for i in advt_list:
        print(i)

    dict_obj = {'advt_list': advt_list,
                'page_obj': page_obj}

    if request.method == "POST":
        dict_obj["searched"] = request.POST["searched"]
        array = []
        for i in advt_list:
            if i.advt_name == dict_obj["searched"]:
                array.append(i)
        if len(array) == 0:
            dict_obj.pop("advt_list", None)
        dict_obj["advt_list"] = array
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
