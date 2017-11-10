from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "sections/about.html"

class ContactView(TemplateView):
    template_name = "sections/contact.html"

class BusinessView(TemplateView):
    template_name = "sections/business.html"

class SportView(TemplateView):
    template_name = "sections/sports.html"

class TechnologyView(TemplateView):
    template_name = "sections/technology.html"

class EntertainmentView(TemplateView):
    template_name = "sections/entertainment.html"

class FashionView(TemplateView):
    template_name = "sections/fashion.html"

class ShortCodeView(TemplateView):
    template_name = "sections/shortcodes.html"

class SingleView(TemplateView):
    template_name = "sections/single.html"

class PrivacyPolicyView(TemplateView):
    template_name = "sections/privacy-policy.html"






