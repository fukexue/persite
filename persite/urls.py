"""persite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from perapp.views import mainindex, noteindex, loginindex, projectindex, messageindex, loginresult, loginout
from perapp.register import registerresult, registerindex

urlpatterns = [
    url(r'^admin/', admin.site.urls,),
    url(r'^mainindex/', mainindex, name='mainindex'),
    url(r'^noteindex/', noteindex, name='noteindex'),
    url(r'^loginindex/', loginindex, name='loginindex'),
    url(r'^projectindex/', projectindex, name='projectindex'),
    url(r'^messageindex/', messageindex, name='messageindex'),
    url(r'^loginresult/', loginresult, name='loginresult'),
    url(r'^register/', registerindex, name='registerindex'),
    url(r'^registerresult/', registerresult, name='registerresult'),
    url(r'^registerresult/', registerresult, name='registerresult'),
    url(r'^loginout/', loginout, name='loginout'),
]
