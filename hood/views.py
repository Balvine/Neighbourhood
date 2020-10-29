from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib.auth.decoraters import login
# Create your views here.

@login_required
def index(request):
    current user = request.user
    try:
        profile = UserProfile.objects.get(user =current_user)
    except:
      return redirect('edit.profile',username=current_user=username)


