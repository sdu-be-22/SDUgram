from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telegrambot.sendMessage import sendTelegram
from grid_panel.models import Advt, Category

# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    advt_list = Advt.objects.all()
    cat_list = Category.objects.all()
    paginator = Paginator(advt_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # for i in advt_list:
    #     print(i)
    price_table = PriceTable.objects.all()
    form = OrderForm()

    dict_obj = {'slider_list': slider_list,
                # 'pc_1': pc_1,
                # 'pc_2': pc_2,
                # 'pc_3': pc_3,
                'page_obj': page_obj,
                'price_table': price_table,
                'form': form,
                'advt_list': advt_list,
                'cat_list': cat_list,
                }

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
searched = 'null'

def advt_detail_view(request):
    advt_list = Advt.objects.all()
    dict_obj = {'advt_list': advt_list}
    global searched
    if request.method == "POST":
        dict_obj["searched"] = request.POST["searched"]
        searched = request.POST["searched"]
        array = []
        # for i in advt_list:
        #     if i.advt_name == searched:
        #         array.append(i)
        # if len(array) == 0:
        #     dict_obj.pop("advt_list", None)
        ser = Advt.objects.filter(advertisement_name__icontains=searched)
        paginator = Paginator(ser, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        dict_obj["page_obj"] = page_obj
    else:
        array = []
        # for i in advt_list:
        #     if i.advt_name == searched:
        #         array.append(i)
        # if len(array) == 0:
        #     dict_obj.pop("advt_list", None)
        ser = Advt.objects.filter(advertisement_name__icontains=searched)
        paginator = Paginator(ser, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        dict_obj["page_obj"] = page_obj
    return render(request, './index.html', dict_obj)