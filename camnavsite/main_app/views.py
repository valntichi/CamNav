from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View

# Create your views here.
from rest_framework.parsers import MultiPartParser, FormParser


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

'''
login API
'''
from django.contrib.auth import authenticate

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        print 'get', request.GET
        return render(request, self.template_name, context={'username':'unknown'})
    def post(self, request):
        context = {}
        print 'post'
        if request.POST['username'] and request.POST['password']:
            context['username'] = request.POST['username']
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user:
                context['authenticated'] = True
                print user
        return render(request, self.template_name, context=context)


from .models import Article, Category
from .serializers import ArticleSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        print 'POST'
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            article = Article()
            article.breaking = serializer.data["breaking"]
            article.title = serializer.data["title"]
            article.content = serializer.data["content"]

            print "Author", serializer.data["author"]
            article.author = User.objects.get(id=serializer.data["author"])
            article.category = Category.objects.get(id=serializer.data["category"])
            article.save()
            # serializer = ArticleSerializer(data=article)
            serializer.data["id"] = article.id
            serializer.data["created_on"] = article.created_on
            return Response(data=serializer.data, status=201)
        else:
            return Response(serializer.errors, 400)

from .serializers import FileListSerializer, PhotoSerializer
from .models import Photo


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset=Photo.objects.all()

    def create(self, request, *args, **kwargs):
        print 'POST'
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            print serializer.data
            return Response(data=serializer.data, status=201)
        else:
            return Response(serializer.errors, 400)