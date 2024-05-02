from django.shortcuts import render, redirect
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages 
from .models import Contact

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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # subject = request.POST.get('subject')
        if name and email and message:
            contact = Contact(full_name=name, email=email, message=message, subject=subject)
            contact.save()
            messages.success(request, 'Message sent successfully')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill all fields')
            return redirect('contact')
    return render(request, 'contact.html')




