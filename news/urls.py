"""
This file defines the URL patterns that are found in the 'news' application,
and specifies to which 'view' each of them is mapped to.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsHomePage.as_view(), name='all-news'),
    path('article/', views.SingleArticlePage.as_view(),
         name='news-detail-page')
]
