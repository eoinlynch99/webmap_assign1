from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_gis.filters import InBBoxFilter
from django.db import models as Entry
from django.shortcuts import render
from django.views import generic
from world.models import Search, GeoSerial

# Create your views here.
class index(generic.TemplateView):
    template_name = 'html.html'