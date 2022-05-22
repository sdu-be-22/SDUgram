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
from django.conf.urls.static import static
from django.conf import settings
from details import views as detail_view
from applyAd import views as applyAd_view
from help import views as help_views
from grid_panel import views as grid_panel
from chat import views as chat_views
from favorite import views as fav_views
from django.contrib.auth import views as auth_views
from aboutAuthor import views as about_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', grid_panel.first_page, name="Home"),
    path('feedbacks/', include('feedbacks.urls'), name='feedback'),
    # path('details/', detail_view.show_details),
    # path('thanks/', views.thanks_page, name = 'thanks_page'),
    # path('signUp/', include("signUp.urls")),
    path('apply/', applyAd_view.apply, name='apply'),
    # path('success', applyAd_view.success, name = 'success'),
    path('myProfile/', include("myProfile.urls"), name='myProfile'),
    path('help/', help_views.help_page),
    path('search/', grid_panel.advt_detail_view, name="Search"),
    path('login/', include("signIN.urls"), name="login"),
    path('register/', include("signUp.urls"), name='register'),
    path('updateUser/', myProfile.views.updateProfile, name='updateUser'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_email.html"),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name='password_reset_complete'),
    # path('favorite_post/',cms_views.favorite_post,name="favorite_post"),
    path('favorites/' ,fav_views.post_favorite_list,name="post_favorite_list"),
    path('category/<slug:cat_slug>/', grid_panel.show_category, name='category'),
    path('today/', grid_panel.show_today, name='today'),
    path('oder_by_date/', grid_panel.order_by_date, name="orderbydate"),
    path('price_max', grid_panel.order_by_priceMax, name="orderbymax"),
    path('price_min', grid_panel.order_by_priceMin, name="orderbymin"),
    path('adver/<int:adver_id>/', detail_view.show_adver, name='adver'),
    path('chat/',chat_views.message_page, name='chat'),
    path('chat/<int:user_id>',chat_views.message_page, name='chat'),
    path('category_info/',grid_panel.count_posts,name='category_info'),
    path('add_favorite/', fav_views.add_favorite, name='add_fav'),
    path('detailsAboutAuthor/<int:id>', about_view.aboutAuthor , name='aboutAuthor'),
    path('team/',grid_panel.teampage, name='team'),
    path('range_price', grid_panel.range_price, name='range_price'),
    path('by_city', grid_panel.by_city, name='by_range'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
