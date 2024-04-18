from django.shortcuts import render, redirect
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages 

@login_required
def dashboard(request):
    user = User.objects.get(username=request.user)
    try:profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        messages.error(request, "Please complete your profile")
        return redirect('user_profile')
    context = {
        'profile': profile,
    }
    return render(request, 'userapp/dashboard.html', context)
