from django import forms
from .models import Job, Resume, Contact, Feedback

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'resume_file', 'cv_picture']
        

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'salary', 'skills', 'company']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'skills': forms.Textarea(attrs={'rows': 5}),
        }


        
    