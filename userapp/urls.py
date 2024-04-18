
from django.urls import path, re_path
from .views import *

urlpatterns = [
    # dashboard
    path('dashboard', dashboard, name='user_dashboard'),
]