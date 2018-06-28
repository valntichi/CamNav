from django.shortcuts import render, redirect
from django.utils.translation import gettext as _

from django.views.generic import TemplateView, View

# Create your views here.
# from rest_framework.parsers import MultiPartParser, FormParser

from .mixins import ExampleMixin


class HomeView(ExampleMixin, TemplateView):
    template_name = "home.html"


class PageCEMMView(TemplateView):
    template_name = "sections/cemm.html"


class OrganisationView(TemplateView):
    template_name = "sections/presentation.html"


class InformationView(TemplateView):
    template_name = "sections/business.html"


class ActionEtatView(TemplateView):
    template_name = "sections/aem.html"


class CCRView(TemplateView):
    template_name = "sections/business.html"


class HistoriqueView(TemplateView):
    template_name = "sections/historique.html"


class ConcoursView(TemplateView):
    template_name = "sections/fashion.html"


class FormationView(TemplateView):
    template_name = "sections/business.html"

class TestView(TemplateView):
    template_name = "sections/test.html"

class SingleView(TemplateView):
    template_name = "sections/single.html"


class PrivacyPolicyView(TemplateView):
    template_name = "sections/privacy-policy.html"


class ContactView(TemplateView):
    template_name = "sections/contact.html"


class TankerView(TemplateView):
    template_name = "sections/tanker.html"
'''
login API
'''
from django.contrib.auth import authenticate


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):

        return render(request, self.template_name, context={'username':'unknown'})

    def post(self, request):
        context = {}

        if request.POST['username'] and request.POST['password']:
            context['username'] = request.POST['username']
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user:
                context['authenticated'] = True
                print user
        return render(request, self.template_name, context=context)
