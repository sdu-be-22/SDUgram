from . import views
from django.urls import path
urlpatterns = [
    path('', views.signUPForm),
    path('submission/', views.submission, name = "submission")
]