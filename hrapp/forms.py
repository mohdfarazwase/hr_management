from django import forms
from .models import Job, Resume, Contact, Feedback

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={'accept': '.pdf, .docx'}),
        }
        

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'salary', 'skills', 'company']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'skills': forms.Textarea(attrs={'rows': 5}),
        }


        
    