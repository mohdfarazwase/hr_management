from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

# job
class Job(models.Model):
    hr = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class JobMatches(models.Model):
    status_choices = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE)
    score = models.IntegerField()
    status = models.CharField(max_length=100, choices=status_choices, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.job.title
# resume
    
class Resume(models.Model):
    file = models.FileField(upload_to='resumes/', help_text='Upload your resume', verbose_name='Resume')  
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.file.path 
   
# contact
    
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
# feedback
    
class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user_name
    
