from datetime import datetime

from django.shortcuts import render, redirect
from .models import Messages
from .forms import *

from django.contrib import messages
# Create your views here.

def message_page(request):
    emails = Messages.objects.filter(to_user = request.user)
    sysdate = datetime.now()
    if request.method == 'POST':
        from_user = request.user
        to_user = request.POST['to_user']
        subject = request.POST['subject']
        message = request.POST['message']
        mesa = Messages(from_user=from_user, to_user=to_user, subject=subject, message=message)
        mesa.save()
        return redirect('chat')
    else:
        form = MessageForm()
    return render(request, 'chat.html', {'form': form, 'emails': emails, 'now_datetime': sysdate})

