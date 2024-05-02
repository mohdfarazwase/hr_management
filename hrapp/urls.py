from django.urls import path, re_path
from .views import *


urlpatterns = [
    # dashboard
    path('dashboard', dashboard, name='hr_dashboard'),    
    path('profile/view', hr_profile_view, name='hr_profile_view'),
    path('profile/edit', hr_profile_edit, name='hr_profile_edit'),
    path('profile/create', hr_profile_create, name='hr_profile_create'),
    # resume list, view, delete, notify
    path('resume/list', resume_list, name='resume_list'),
    path('resume/view/<int:id>', resume_view, name='resume_view'),
    path('resume/delete/<int:id>', resume_delete, name='resume_delete'),
    path('resume/notify/<int:id>', resume_notify, name='resume_notify'),
    # job list, add, view, edit, delete
    path('job/list', job_list, name='job_list'),
    path('job/add', job_add, name='job_add'),
    path('job/view/<int:id>', job_view, name='job_view'),
    path('job/edit/<int:id>', job_edit, name='job_edit'),
    path('job/delete/<int:id>', job_delete, name='job_delete'),
    path('job/match/<int:id>', job_match, name='job_match'),
]