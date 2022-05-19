from datetime import datetime

from django.shortcuts import render, redirect
from .models import Messages
from .forms import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages


def message_page(request, user_id=None):
    if not request.user.is_authenticated:
        return redirect('login')
    if user_id:
        emails = Messages.objects.filter(to_user=request.user, from_user=user_id)
    else:
        emails = Messages.objects.filter(to_user=request.user)
    users = []
    for e in Messages.objects.filter(to_user=request.user):
        users.append(e.from_user)
    users = set(users)
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
    return render(request, 'chat.html', {'form': form,
                                         'emails': emails,
                                         'now_datetime': sysdate,
                                         'users': users,
                                         })
