from . import views
from django.urls import path
urlpatterns = [
    path('', views.signUPForm, name="signUP"),
    path('submission/', views.submission, name = "submission")
]