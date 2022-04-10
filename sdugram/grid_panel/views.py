import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from grid_panel.models import Advt, Category

# Create your views here.

def show_category(request, cat_id):
    advt_list = Advt.objects.filter(advertisement_category=cat_id)
    cat_list = Category.objects.all()
    paginator = Paginator(advt_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dict_obj = {
        'page_obj': page_obj,
        'advt_list': advt_list,
        'cat_list': cat_list,
        'selected': cat_id,
    }
    return render(request, './index.html', dict_obj)

def show_today(request):

    advt_list = Advt.objects.filter(advt_dt__gte=datetime.date.today())
    cat_list = Category.objects.all()
    paginator = Paginator(advt_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dict_obj = {
        'page_obj': page_obj,
        'advt_list': advt_list,
        'cat_list': cat_list
    }
    return render(request, './index.html', dict_obj)

def order_by_date(request):
    advt_list = Advt.objects.all().order_by('-advt_dt')
    cat_list = Category.objects.all()
    paginator = Paginator(advt_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dict_obj = {
        'page_obj': page_obj,
        'advt_list': advt_list,
        'cat_list': cat_list
    }
    return render(request, './index.html', dict_obj)

def order_by_priceMax(request):
    advt_list = Advt.objects.all().order_by('-advt_price')
    cat_list = Category.objects.all()
    paginator = Paginator(advt_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dict_obj = {
        'page_obj': page_obj,
        'advt_list': advt_list,
        'cat_list': cat_list
    }
    return render(request, './index.html', dict_obj)

def order_by_priceMin(request):
    advt_list = Advt.objects.all().order_by('advt_price')
    cat_list = Category.objects.all()
    paginator = Paginator(advt_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dict_obj = {
        'page_obj': page_obj,
        'advt_list': advt_list,
        'cat_list': cat_list
    }
    return render(request, './index.html', dict_obj)

