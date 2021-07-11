"""
This file contains all the functions/classes that will render (provide the views for)
the endpoints for the 'vida' application
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def home(request: HttpRequest) -> HttpResponse:
    """
    The function in charge of rendering the '/' endpoint.
    """
    return render(request, 'vida/home.html')

def about(request: HttpRequest) -> HttpResponse:
    """
    The function in charge of rendering the 'about/' endpoint.
    """
    # Additional context to pass down.
    context = {
        'title': 'About Us'
    }
    return render(request, 'vida/about.html', context)
  