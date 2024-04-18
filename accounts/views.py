from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .forms import HrProfileForm, UserProfileForm
from .models import HrProfile, UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def hr_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        group = request.POST.get('group') # customer
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, 'Invalid credentials')
                redirect('hlogin')
            else:
                # if user is a customer
                if user.groups.filter(name=group).exists():
                    login(request, user)
                    request.session['group'] = group
                    messages.success(request, 'Welcome, ' + user.username)
                    return redirect('home')
                else:
                    messages.error(request, 'You are not a hr')
                    return redirect('hlogin')
        else:
            messages.error(request, 'Please fill all fields')
    return render(request, 'accounts/hr/login.html')
def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        group = request.POST.get('group') 
        print(group, username, password)
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, 'Invalid credentials')
                redirect('ulogin')
            else:
                # if user is a hr
                if user.groups.filter(name=group).exists():
                    login(request, user)
                    request.session['group'] = group
                    return redirect('user_dashboard')
                else:
                    messages.error(request, 'You are not a user')
                    return redirect('ulogin')
        else:
            messages.error(request, 'Please fill all fields')
    return render(request, 'accounts/user/login.html')
    
def hr_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        group = request.POST['group']
        if pwd1 == pwd2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=pwd1)
                user.save()
                group = Group.objects.get(name=group)
                user.groups.add(group)
                messages.success(request, 'Account successfully created')
                return redirect('hregister')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'accounts/hr/register.html')
def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        group = request.POST['group']
        if pwd1 == pwd2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=pwd1)
                user.save()
                group = Group.objects.get(name=group)
                user.groups.add(group)
                messages.success(request, 'Account successfully created')
                return redirect('uregister')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'accounts/user/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def user_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('user_profile')
    ctx = {
        'form': form
    }
    return render(request, 'accounts/user/profile.html', ctx)

@login_required
def hr_profile(request):
    form = HrProfileForm()
    if request.method == 'POST':
        hr_form = HrProfileForm(request.POST, request.FILES, instance=request.user.hrprofile)
        if hr_form.is_valid():
            hr_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('hr_profile')
    ctx = {
        'form': form
    }
    return render(request, 'accounts/hr/profile.html', ctx)
