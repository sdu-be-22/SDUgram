import datetime

from django.core.paginator import Paginator
from django.core.validators import validate_image_file_extension
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from grid_panel.models import Advt, Category
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.

def first_page(request):
    advt_list = Advt.objects.all()
    if request.POST.get('city'):
        advt_list = Advt.objects.filter(advertisement_location=request.POST.get('city'))
    cat_list = Category.objects.all()
    paginator = Paginator(advt_list, 3)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    dict_obj = {'page_obj': page_obj,
                'advt_list': advt_list,
                'cat_list': cat_list,
                }

    return render(request, './index.html', dict_obj)


def show_category(request, cat_slug):
    category = Category.objects.get(slug=cat_slug)
    advt_list = Advt.objects.filter(advertisement_category=category.pk)
    cat_list = Category.objects.all()
    paginator = Paginator(advt_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dict_obj = {
        'page_obj': page_obj,
        'advt_list': advt_list,
        'cat_list': cat_list,
        'selected': cat_slug,
    }
    return render(request, 'index.html', dict_obj)


def show_today(request):
    # advt_list = Advt.objects.filter(advertisement_date_created__gte=datetime.date.today())
    advt_list = request.GET.get('advt_list')
    cat_list = Category.objects.all()
    paginator = Paginator(advt_list, 10)
    page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    dict_obj = {
        # 'page_obj': page_obj,
        'advt_list': advt_list,
        'cat_list': cat_list
    }

    return render(request, 'index.html', dict_obj)


def order_by_date(request):
    advt_list = Advt.objects.all().order_by('-advertisement_date_created')
    cat_list = Category.objects.all()
    paginator = Paginator(advt_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dict_obj = {
        'page_obj': page_obj,
        'advt_list': advt_list,
        'cat_list': cat_list
    }
    return render(request, 'index.html', dict_obj)


def order_by_priceMax(request):
    advt_list = Advt.objects.all().order_by('-advertisement_price')
    cat_list = Category.objects.all()
    paginator = Paginator(advt_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dict_obj = {
        'page_obj': page_obj,
        'advt_list': advt_list,
        'cat_list': cat_list
    }
    return render(request, 'index.html', dict_obj)


def order_by_priceMin(request):
    advt_list = Advt.objects.all().order_by('advertisement_price')
    cat_list = Category.objects.all()
    paginator = Paginator(advt_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dict_obj = {
        'page_obj': page_obj,
        'advt_list': advt_list,
        'cat_list': cat_list
    }
    return render(request, 'index.html', dict_obj)


def range_price(request):
    # print('debug', request.POST.get('typeNumber'))
    num1 = request.POST.get('typeNumber')
    num2 = request.POST.get('typeNumber2')
    print(num1)
    print(num2)
    advt_list = Advt.objects.filter(advertisement_price__range=[num1, num2])
    print(advt_list)
    cat_list = Category.objects.all()
    paginator = Paginator(advt_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dict_obj = {
        'page_obj': page_obj,
        'advt_list': advt_list,
        'cat_list': cat_list,
        'range_num1': num1,
        'range_num2': num2,
    }
    return render(request, 'index.html', dict_obj)


def by_city(request):
    advt_list = Advt.objects.all()
    if request.POST.get('city'):
        advt_list = Advt.objects.filter(advertisement_location=request.POST.get('city'))
    cat_list = Category.objects.all()
    paginator = Paginator(advt_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dict_obj = {
        'page_obj': page_obj,
        'advt_list': advt_list,
        'cat_list': cat_list,
    }

    return JsonResponse(serialize('json', advt_list, cls=LazyEncoder), safe=False)


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Advt):
            return str(obj)
        return super().default(obj)


def count_posts(request):
    services = Advt.objects.filter(advertisement_category=1).count()
    job = Advt.objects.filter(advertisement_category=2).count()
    transport = Advt.objects.filter(advertisement_category=3).count()
    real_estate = Advt.objects.filter(advertisement_category=4).count()
    fashion = Advt.objects.filter(advertisement_category=5).count()
    animals = Advt.objects.filter(advertisement_category=6).count()
    electronics = Advt.objects.filter(advertisement_category=7).count()
    childworld = Advt.objects.filter(advertisement_category=8).count()
    giveaways = Advt.objects.filter(advertisement_category=9).count()
    houseandgarden = Advt.objects.filter(advertisement_category=10).count()
    sports = Advt.objects.filter(advertisement_category=11).count()

    ers = {'services': services,
           'job': job,
           'transport': transport,
           'real_estate': real_estate,
           'fashion': fashion,
           'animals': animals,
           'electronics': electronics,
           'childworld': childworld,
           'giveaways': giveaways,
           'houseandgarden': houseandgarden,
           'sports': sports}

    return render(request, 'category_info.html', ers)


def teampage(request):
    return render(request, 'team.html')


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
