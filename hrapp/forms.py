from django import forms
from .models import Resume
from .models import Contact
class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'resume_file', 'cv_picture']
        

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        
    