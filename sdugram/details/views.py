from django.http import HttpResponse
from django.shortcuts import render
from crm.models import Order
from cms.models import CmsSlider
from feedbacks.models import FeedbackItemModel
from grid_panel.models import Advt, Category
# Create your views here.
from details.forms import OrderForm
from feedbacks.forms import FeedBackItemForm


def show_details(request):
    cms_slider = CmsSlider.objects.all()

    item_about = "Точную цену для Вашего авто, уточняйте у менеджера. Цена зависит от выбранного комплекта. 1. Чистый салон в любое время года: Благодаря уникальной ячеистой структуре, коврики блокируют грязь, снег и воду. За счёт этого даже в период непогоды ваша обувь, одежда и салон остаются чистыми. 2. Влага: коврики Ева не нуждаются в просушке. Материал ковриков не впитывает воду, что гарантирует вам отсутствие неприятных запахов в жару и предотвращает образование плесени. 3. Отличное крепление: за счёт липучек и штатных креплений коврики п лотно прилегают к поверхности пола и не скользят в период эксплуатации. 4. Прочность и долговечность: Использовать коврики вы можете круглый год при температуре от — 60 до + 80. Они сохраняют эластичность в суровые морозы и не теряют прочность в жару. Как показывает опыт, коврики Ева достойно служат своим владельцам до 10 лет."
    d = {"slider_list": cms_slider, "first_name": "Zhandos", "was_online": "12:32", "location": "Актобе, Казахстан",
         "item_name": "Коврики(полики) от EVA SHOP(ЭВА,ЕВА) уже в Казахстане..", "item_price": "12 000тг",
         "item_detail": item_about, "form": OrderForm()}
    return render(request, "./detail.html", d)


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, './thanks.html', {'name': name,
                                             'phone': phone})

def show_adver(request, adver_id):
    advt = Advt.objects.filter(pk=adver_id).first
    form = FeedBackItemForm()

    dict = {
        'advt': advt,
        'form': form,
        "list": FeedbackItemModel.objects.filter(item=adver_id),
        'adver_id': adver_id
    }
    return render(request, 'details/adver_full_info.html', dict)
