from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from world.models import Search

# Register your models here.
@admin.register(Search)
class EntryAdmin(OSMGeoAdmin):
    class EntryAdmin(OSMGeoAdmin):
        default_lon = 53337065
        default_lat = 6267533
        default_zoom = 12
