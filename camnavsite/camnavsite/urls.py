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


from main_app.views import (HomeView,PageCEMMView,OrganisationView, InformationView,
                            ActionEtatView, CCRView,
                            HistoriqueView,FormationView, CouncoursView
                            )


urlpatterns = i18n_patterns (
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="accueil"),
    url(r'^cemm/$', PageCEMMView.as_view(), name="page-cemm"),
    url(r'^organisation/$', OrganisationView.as_view(), name="organisation"),
    url(r'^information/$', InformationView.as_view(), name="information"),
    url(r'^historique/$', HistoriqueView.as_view(), name="historique"),
    url(r'^action-etat-mer/$', ActionEtatView.as_view(), name="action-etat-mer"),
    url(r'^ccr/$', CCRView.as_view(), name="ccr"),
    url(r'^formations/$', FormationView.as_view(), name="formations"),
    url(r'^concours/$', CouncoursView.as_view(), name="councours"),

)
urlpatterns += staticfiles_urlpatterns()