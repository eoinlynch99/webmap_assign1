"""webmap_assign1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from urllib import request

from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render
from django.template import context
from django.urls import path, include
from django.views.generic import TemplateView
from world import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index.as_view()),
    path('', views.sendit),
]


def sendit():
    return render(request, 'html.html')
