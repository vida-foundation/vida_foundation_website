"""
This file defines the URL patterns that are found in the 'vida' application,
and specifies to which 'view' each of them is mapped to.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='vida-foundation-home'),
    path('about/', views.about, name='vida-foundation-about')
]
