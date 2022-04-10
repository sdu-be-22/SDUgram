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
    1. Import the include() function: from django   .urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
import myProfile.views
from crm import views
from cms import views as cms_views
from django.conf.urls.static import static
from django.conf import settings
from details import views as detail_view
from applyAd import views as applyAd_view
from help import views as help_views
from grid_panel import views as grid_panel
from chat import views as chat_views
from message import views as message

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('message/', include("message.urls")),
    path('', views.first_page, name="Home"),
    path('feedbacks/', include('feedbacks.urls'), name="feedback"),
    path('details/', detail_view.show_details),
    path('advertisements/', views.Adboard, name = 'advertisements'),
    path('thanks/', views.thanks_page, name = 'thanks_page'),
    path('signUp/', include("signUp.urls")),
    path('apply/', applyAd_view.image_view, name='apply'),
    path('success', applyAd_view.success, name = 'success'),
    path('myProfile/', include("myProfile.urls"), name='myProfile'),
    path('help/', help_views.help_page),
    path('search/', views.advt_detail_view, name="Search"),
    path('login/', include("signIN.urls"), name='login'),
    path('register/', include("signUp.urls"), name='register'),
    path('updateUser/', myProfile.views.updateProfile, name='updateUser'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('favorite_post/',cms_views.favorite_post,name="favorite_post"),
    path('favorites/' ,cms_views.post_favorite_list,name="post_favorite_list"),
    path('add_fav<int:id>', cms_views.add_fav, name='add_fav'),
    path('category/<int:cat_id>/', grid_panel.show_category, name='category'),
    path('today/', grid_panel.show_today, name='today'),
    path('oder_by_date/', grid_panel.order_by_date, name="orderbydate"),
    path('price_max', grid_panel.order_by_priceMax, name="orderbymax"),
    path('price_min', grid_panel.order_by_priceMin, name="orderbymin"),
    path('adver/<int:adver_id>/', detail_view.show_adver, name='adver'),
    path('chat/',chat_views.message_page, name='chat')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
