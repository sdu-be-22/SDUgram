from django.shortcuts import render
from django.contrib.auth.models import User
from grid_panel.models import Advt

# Create your views here.
def aboutAuthor(request, id):
    user = User.objects.get(pk=id)
    items = Advt.objects.filter(advertisement_user = user)
    # for u in user:
    #     items = Advt.objects.filter(advertisement_user=u.pk)
    #
    # user = user.first

    dict = {"user": user, "items": items}
    return render(request, "aboutAuthor.html", dict)

