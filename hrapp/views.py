from django.shortcuts import render, redirect
from accounts.models import HrProfile
from accounts.forms import HrProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
# Create your views here.

@login_required
def dashboard(request):
    user = User.objects.get(username=request.user)
    try:profile = HrProfile.objects.get(user=user)
    except: 
        messages.warning(request, 'Please create your profile first')
        return redirect('hr_profile_create')
    context = {
        'profile': profile,
    }
    return render(request, 'hrapp/dashboard.html', context)

@login_required
def hr_profile_create(request):
    user = User.objects.get(username=request.user)
    form = HrProfileForm()
    if request.method == 'POST':
        form = HrProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Profile created successfully')
            return redirect('hr_dashboard')
    context = {
        'form': form,
    }
    return render(request, 'hrapp/profile_form.html', context)

@login_required
def hr_profile_view(request):
    user = User.objects.get(username=request.user)
    try:profile = HrProfile.objects.get(user=user)
    except: 
        messages.warning(request, 'Please create your profile first')
        return redirect('hr_profile_create')
    context = {
        'profile': profile,
    }
    return render(request, 'hrapp/profile_view.html', context)

@login_required
def hr_profile_edit(request):
    user = User.objects.get(username=request.user)
    try:profile = HrProfile.objects.get(user=user)
    except: 
        messages.warning(request, 'Please create your profile first')
        return redirect('hr_profile_create')
    form = HrProfileForm(instance=profile)
    if request.method == 'POST':
        form = HrProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('hr_profile_view')
    context = {
        'form': form,
    }
    return render(request, 'hrapp/profile_form.html', context)


@login_required
def resume_list(request):
    user = User.objects.get(username=request.user)
    profile = HrProfile.objects.get(user=user)
    context = {
        'profile': profile,
    }
    return render(request, 'hrapp/resume_list.html', context)
 
@login_required
def contact_view(request):
    user = User.objects.get(username=request.user)
    profile = HrProfile.objects.get(user=user)
    context = {
        'profile': profile,
    }
    return render(request, 'hrapp/contact.html', context)
