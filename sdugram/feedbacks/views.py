from django.shortcuts import render,redirect
from .models import FeedbackItemModel, FeedbackModel
from .forms import FeedbackForm
from django.contrib import messages

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
  messages.success(request, f'Thanks for feedback! {request.user.username}')
  return redirect('comments')


def thanks_id(request, advertisement_id):
  description = request.POST['description']
  model = FeedbackItemModel(caption=description, user=request.user, item=advertisement_id)
  model.save()
  return render(request, 'feedbacks/thanks.html')