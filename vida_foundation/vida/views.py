from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'vida/home.html')

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'vida/about.html')
