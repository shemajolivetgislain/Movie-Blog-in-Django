
from typing import Pattern
from django import urls
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name="index"),
    # path('registration', register, name='registration')
]
