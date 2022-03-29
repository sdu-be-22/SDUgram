from django.shortcuts import render
from .models import FeedbackModel
from .forms import FeedbackForm


# Create your views here.
def feedbacks(request):
    list_feedbacks = {"list": FeedbackModel.objects.all(), "count": len(FeedbackModel.objects.all())}
    return render(request, "feedbacks/feedbacks.html", list_feedbacks)


def addFeedbacks(request):
  form = FeedbackForm()
  return render(request, 'feedbacks/feedbacks_add.html', {'form': form})


def thanks(request):
  title = request.POST['title']
  description = request.POST['description']
  model = FeedbackModel(name=title, caption=description)
  model.save()
  return render(request, 'feedbacks/thanks.html')