from django import forms

from .models import HrProfile, UserProfile

class HrProfileForm(forms.ModelForm):
    class Meta:
        model = HrProfile
        fields = ['picture', 'first_name', 'last_name', 'gender',  'bio']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture', 'first_name', 'last_name', 'gender',  'bio']
        