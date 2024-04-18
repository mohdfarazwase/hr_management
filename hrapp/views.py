from django.shortcuts import render
from accounts.models import HrProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
# Create your views here.

@login_required
def dashboard(request):
    user = User.objects.get(username=request.user)
    profile = HrProfile.objects.get(user=user)
    context = {
        'profile': profile,
    }
    return render(request, 'hrapp/dashboard.html', context)