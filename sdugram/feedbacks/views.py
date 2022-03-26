from django.shortcuts import render
from .models import FeedbackModel
# Create your views here.
def feedbacks(request):
    list_feedbacks = {"list": FeedbackModel.objects.all(), "count": len(FeedbackModel.objects.all())}
    return render(request, "feedbacks/feedbacks.html", list_feedbacks)

def addFeedbacks(request):
    None
