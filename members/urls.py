from typing import Pattern
from django import urls
from django.conf.urls import include
from django.urls import path
from .views import ShowProfilePageView, UserEditProfile, UserRegisterView, dashboard


urlpatterns = [
    path('register/', UserRegisterView.as_view(),  name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('edit_profile/', UserEditProfile, name='edit_profile'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='show_profile')
]
