from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout_user, name='logout')

]