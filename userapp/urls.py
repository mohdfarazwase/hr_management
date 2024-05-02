
from django.urls import path, re_path
from .views import *
from .views import dashboard, contact_view

urlpatterns = [
    # dashboard
    path('dashboard', dashboard, name='user_dashboard'),

    # contact
    path('contact', contact_view, name='contact'),
    
]