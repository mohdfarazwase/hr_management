
from django.urls import path, re_path
from .views import *
from .views import dashboard, contact_view, contact_create, contact_edit, contact_delete

urlpatterns = [
    # dashboard
    path('dashboard', dashboard, name='user_dashboard'),

    # contact
    path('contact', contact_view, name='contact'),
    path('contact/create', contact_create, name='contact_create'),
    path('contact/edit/<int:id>', contact_edit, name='contact_edit'),
    path('contact/delete/<int:id>', contact_delete, name='contact_delete'),
]