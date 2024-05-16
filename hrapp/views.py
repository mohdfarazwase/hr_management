from django.shortcuts import render, redirect
from accounts.models import HrProfile
from accounts.forms import HrProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .models import Job, JobMatches, Resume, Contact, Feedback
from .forms import JobForm
from common.resume_analyzer import match_resume_with_job
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import UserProfile
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
    resumes = Resume.objects.all()
    ctx = {
        'resumes': resumes,
    }
    return render(request, 'hrapp/resume_list.html', ctx)

@login_required
def resume_view(request, id):
    resume = Resume.objects.get(id=id)
    ctx = {
        'resume': resume,
    }
    return render(request, 'hrapp/resume_view.html', ctx)

@login_required
def resume_delete(request, id):
    resume = Resume.objects.get(id=id)
    resume.delete()
    messages.success(request, 'Resume deleted successfully')
    return redirect('resume_list')

@login_required
def resume_notify(request, id):
    resume = Resume.objects.get(id=id)
    subject = 'Job opportunity'
    message = 'Your resume has been shortlisted for a job opportunity. Please check the job listing for more details.'
    email_from = settings.EMAIL_HOST_USER
    applicant = resume.user
    try:
        applicant_profile = UserProfile.objects.get(user=applicant)
        recipient_list = [resume.user.email]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'Notification sent successfully')
        return redirect('job_list')
    except Exception as e:
        print(e)
        messages.error(request, 'Error sending notification')
        return redirect('job_list')
  
# job views
@login_required
def job_list(request):
    hr = request.user
    jobs = Job.objects.filter(hr=hr).order_by('-created_at')
    context = {
        'jobs': jobs,
    }
    return render(request, 'hrapp/job_list.html', context)

@login_required
def job_add(request):
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.hr = request.user
            job.save()
            messages.success(request, 'Job added successfully')
            return redirect('job_list')
    context = {'form': form, }
    return render(request, 'hrapp/job_form.html', context)

@login_required
def job_view(request, id):
    job = Job.objects.get(id=id)
    context = {'job': job,}
    return render(request, 'hrapp/job_view.html', context)

@login_required
def job_edit(request, id):
    job = Job.objects.get(id=id)
    form = JobForm(instance=job)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully')
            return redirect('job_list')
    context = {'form': form,}
    return render(request, 'hrapp/job_form.html', context)

@login_required
def job_delete(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    messages.success(request, 'Job deleted successfully')
    return redirect('job_list')

@login_required
def job_match(request, id):
    job = Job.objects.get(id=id)
    resumes = Resume.objects.all()
    job_matches = JobMatches.objects.filter(job=job).order_by('-score')
    for resume in resumes:
        # if resume in job matches, skip
        if JobMatches.objects.filter(job=job, resume=resume).exists():
            continue
        print(resume)
        file = resume.file
        match_resume_with_job(job_id=job.id, resumes=[resume])
    context = {
        'job': job,
        'resumes': resumes,
        'job_matches': job_matches,
    }
    return render(request, 'hrapp/job_match.html', context)

@login_required
def job_matches_delete(request, id):
    try:
        job_match = JobMatches.objects.get(id=id)
        job_match.delete()
        messages.success(request, 'Job match deleted successfully')
    except:
        messages.error(request, 'Error deleting job match')
    return redirect('job_match', job_match.job.id)


