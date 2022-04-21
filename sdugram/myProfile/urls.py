from django.urls import path
from .views import *

myProfile = 'myProfile'
urlpatterns = [
    path('', main_page, name='myProfile'),
    path('myAdvertisements/', show_my_advertisements, name='myAdvertisements'),
    path('updateProfile/', updateProfile, name='updateProfile'),
    path('myAdvertisements/<int:adver_id>/', editAdver, name='edit'),
]