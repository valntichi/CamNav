from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"