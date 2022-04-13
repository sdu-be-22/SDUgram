from django.urls import path
from .views import *
urlpatterns = [
    path('', main_page, name='myProfile'),
    path('updateProfile/', updateProfile, name='updateProfile'),
    path('myAdvertisements/', show_my_advertisements, name='myAdvertisements')
]