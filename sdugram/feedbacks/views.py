from django.shortcuts import render
from .models import FeedbackItemModel, FeedbackModel
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
  model = FeedbackModel(name=title, caption=description, user=request.user)
  model.save()
  return render(request, 'feedbacks/thanks.html')


def thanks(request, adver_id):
  description = request.POST['description']
  model = FeedbackItemModel(caption=description, user=request.user, item=adver_id)
  model.save()
  return render(request, 'feedbacks/thanks.html')