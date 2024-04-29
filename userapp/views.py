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


@login_required
def contact_view(request):
    user = User.objects.get(username=request.user)
    profile = UserProfile.objects.get(user=user)
    context = {
        'profile': profile,
    }
    return render(request, 'hrapp/contact.html', context)

@login_required
def contact_create(request):
    user = User.objects.get(username=request.user)
    profile = UserProfile.objects.get(user=user)
    context = {
        'profile': profile,
    }
    return render(request, 'hrapp/contact_form.html', context)

@login_required
def contact_edit(request, id):
    user = User.objects.get(username=request.user)
    profile = UserProfile.objects.get(user=user)
    context = {
        'profile': profile,
    }
    return render(request, 'hrapp/contact_form.html', context)

@login_required
def contact_delete(request, id):
    user = User.objects.get(username=request.user)
    profile = UserProfile.objects.get(user=user)
    context = {
        'profile': profile,
    }
    return render(request, 'hrapp/contact.html', context)
