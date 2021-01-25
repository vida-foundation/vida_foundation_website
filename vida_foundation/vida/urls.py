from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='vida-foundation-home'),
    path('about/', views.about, name='vida-foundation-about')
]
