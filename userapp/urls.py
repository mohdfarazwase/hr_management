
from django.urls import path, re_path
from .views import *
from .views import dashboard, contact_view , feedback

urlpatterns = [
    # dashboard
    path('dashboard', dashboard, name='user_dashboard'),
    path('user/profile', user_profile, name='user_profile'),
    path('user/profile/edit', user_profile_edit, name='user_profile_edit'),
    path('upload/cv', upload_resume, name='uploadcv'),

    # contact
    path('contact', contact_view, name='contact'),
    # resume upload
    path('resume/upload', resume_upload, name='resume_upload'),
    path('myresume/list', myresume_list, name='myresume_list'),
    path('myresume/view/<int:id>', myresume_view, name='myresume_view'),
    path('myresume/delete/<int:id>', myresume_delete, name='myresume_delete'),
    #feedback
    path('feedback', feedback, name='feedback'),



]