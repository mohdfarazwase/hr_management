from django.urls import path, re_path
from .views import *


urlpatterns = [
    # dashboard
    path('dashboard', dashboard, name='hr_dashboard'),    
    path('profile/view', hr_profile_view, name='hr_profile_view'),
    path('profile/edit', hr_profile_edit, name='hr_profile_edit'),
    path('profile/create', hr_profile_create, name='hr_profile_create'),
    # resume
    path('resume/list', resume_list, name='resume_list'),

    # contact
    path('contact', contact_view, name='contact'),
    
]