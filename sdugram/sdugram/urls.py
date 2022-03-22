"""sdugram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import myProfile.views
from crm import views
from django.conf.urls.static import static
from django.conf import settings
from details import views as detail_view
from applyAd import views as applyAd_view
from help import views as help_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page, name="Home"),
    path('details/', detail_view.show_details),
    path('advertisements/', views.Adboard, name = 'advertisements'),
    path('thanks/', views.thanks_page, name = 'thanks_page'),
    path('signUp/', include("signUp.urls")),
    path('apply/', applyAd_view.image_view, name='apply'),
    path('success', applyAd_view.success, name = 'success'),
    path('myProfile/', myProfile.views.main_page, name='myProfile'),
    path('help/', help_views.help_page),
    path('search/', views.advt_detail_view, name="Search"),
    path('login/', include("signIN.urls"), name='login'),
    path('register/', include("signUp.urls"), name='register'),
    path('updateUser/', myProfile.views.updateProfile, name='updateUser'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
