from django.urls import path
from . import views


urlpatterns = [
    path('', views.feedbacks, name="comments"),
    path('add/', views.addFeedbacks, name="add_feedback"),
    path('thanks/', views.thanks, name="thanks")
]
