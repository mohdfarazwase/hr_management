from django.shortcuts import render, redirect
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages 
from .models import Contact
from hrapp.models import Resume
from hrapp.forms import ResumeForm
from accounts.forms import UserProfileForm

@login_required
def dashboard(request):
    user = User.objects.get(username=request.user)
    # resume form
    try:profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        messages.error(request, "Please complete your profile")
        return redirect('user_profile')
    resume_form = ResumeForm()
    resume_list = Resume.objects.filter(user=user)[:3]
    context = {
        'profile': profile,
        'resume_form': resume_form,
        'resume_list': resume_list,
    }
    return render(request, 'userapp/dashboard.html', context)


@login_required
def user_profile(request):
    form = UserProfileForm()
    profile = UserProfile.objects.filter(user=request.user).first()
    if profile:
        form = UserProfileForm(instance=profile)
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid():
            form = user_form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('user_profile')
    ctx = {'form': form}
    return render(request, 'userapp/profile.html', ctx)

@login_required
def user_profile_edit(request):
    user = User.objects.get(username=request.user)
    try:profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        messages.error(request, "Please complete your profile")
        return redirect('user_profile')
    form = UserProfileForm(instance=profile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('user_profile')
    context = {
        'form': form,
    }
    return render(request, 'userapp/profile_edit.html', context)

@login_required
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # subject = request.POST.get('subject')
        if name and email and message:
            contact = Contact(full_name=name, email=email, message=message, subject=sujbect)
            contact.save()
            messages.success(request, 'Message sent successfully')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill all fields')
            return redirect('contact')
    return render(request, 'contact.html')


@login_required
def upload_resume(request):
    form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            messages.success(request, 'Resume uploaded successfully')
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Please fill all fields')
            return redirect('user_dashboard')
    context = {
        'form': form,
    }
    return render(request, 'userapp/uploadcv.html', context)

# resume upload
@login_required
def resume_upload(request):
    # check user group
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            messages.success(request, 'Resume uploaded successfully')
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Please fill all fields')
            return redirect('user_dashboard')
    

@login_required
def myresume_list(request):
    user = User.objects.get(username=request.user)
    try:profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        messages.error(request, "Please complete your profile")
        return redirect('user_profile')
    resumes = Resume.objects.filter(user=user)
    print(resumes)
    context = {
        'resumes': resumes,
    }
    return render(request, 'userapp/resume_list.html', context)

@login_required
def myresume_view(request, id):
    user = User.objects.get(username=request.user)
    try:profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        messages.error(request, "Please complete your profile")
        return redirect('user_profile')
    resume = Resume.objects.get(id=id)
    context = {
        'resume': resume,
    }

    response = render(request, 'userapp/resume_view.html', context)
    response['X-Frame-Options'] = 'allow-from *'
    return response

@login_required
def myresume_delete(request, id):
    user = User.objects.get(username=request.user)
    try:profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        messages.error(request, "Please complete your profile")
        return redirect('user_profile')
    resume = Resume.objects.get(id=id)
    resume.delete()
    messages.success(request, 'Resume deleted successfully')
    return redirect('myresume_list')

@login_required
def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            contact = Contact(full_name=name, email=email, message=message)
            contact.save()
            messages.success(request, 'Feedback sent successfully')
            return redirect('feedback')
        else:
            messages.error(request, 'Please fill all fields')
            return redirect('feedback')
    return render(request, 'feedback.html')






