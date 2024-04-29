from django.urls import path, re_path
from .views import *
from .views import dashboard, hr_profile_view, hr_profile_edit, hr_profile_create, resume_list, contact_view, contact_create, contact_edit, contact_delete


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
    path('contact/create', contact_create, name='contact_create'),
    path('contact/edit/<int:id>', contact_edit, name='contact_edit'),
    path('contact/delete/<int:id>', contact_delete, name='contact_delete'),

    
]