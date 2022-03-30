
from importlib.resources import path

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('<str:room>/', views.room, name='message'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]
