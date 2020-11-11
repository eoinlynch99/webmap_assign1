from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django.contrib.gis.db import models
from django import forms

class Place(forms.Form):
    placeName = forms.IntegerField()
    geoName = models.TextField()

class GeoSerial(GeoFeatureModelSerializer):
    class Meta:
        geo_field = 'City'
        fields = ('id',)

class Search(models.Model):
    cityName = models.CharField(max_length=255)
    lat = models.PointField()
    long = models.PointField()

    def __str__(self):
        return self.cityName
