from django.shortcuts import render
from typing import List
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from django.views import View
from django.urls import reverse

# Create your views here.


class NewsHomePage(View):
    def get(self, request):
        return render(request, "news/index.html")


class SingleArticlePage(View):
    def get(self, request):
        return render(request, "news/article-detail.html")
