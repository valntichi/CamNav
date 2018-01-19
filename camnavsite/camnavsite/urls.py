"""camnavsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns


from main_app.views import HomeView, AboutView, ContactView, BusinessView, SportView, TechnologyView, EntertainmentView,\
ShortCodeView, FashionView, SingleView, PrivacyPolicyView

from main_app.views import LoginView, ArticleViewSet, PhotoViewSet, PeopleView, my_view

urlpatterns = i18n_patterns (
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^about/$', AboutView.as_view(), name="about"),
    url(r'^contact/$', ContactView.as_view(), name="contact"),
    url(r'^business/$', BusinessView.as_view(), name="business"),
    url(r'^entertainment/$', EntertainmentView.as_view(), name="entertainment"),
    url(r'^sports/$', SportView.as_view(), name="sports"),
    url(r'^technology/$', TechnologyView.as_view(), name="technology"),
    url(r'^shortcodes/$', ShortCodeView.as_view(), name="shortcodes"),
    url(r'^fashion/$', FashionView.as_view(), name="fashion"),
    url(r'^single/$', SingleView.as_view(), name="single"),
    url(r'^privacy-policy/$', PrivacyPolicyView.as_view(), name="privacy-policy"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^translate/$', my_view, name="translate"),


    url(r'^api/v1/articles/$', ArticleViewSet.as_view({'get': 'list', 'post': 'create'}), name="article"),
    url(r'^api/v1/photos/$', PhotoViewSet.as_view({'get': 'list', 'post': 'create'}), name="photo"),

    url(r'^people/$', PeopleView.as_view(), name="people"),

)
urlpatterns += staticfiles_urlpatterns()