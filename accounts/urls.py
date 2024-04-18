from django.urls import path
from . import views

urlpatterns = [
    path("h/login", views.hr_login, name="hlogin"),
    path("u/login", views.user_login, name="ulogin"),
    path("h/register", views.hr_register, name="hregister"),
    path("u/register", views.user_register, name="uregister"),
    path('logout', views.logout_view, name='logout'),
    #  profiles
    path('hr/profile', views.hr_profile, name='hr_profile'),
    path('user/profile', views.user_profile, name='user_profile'),
]