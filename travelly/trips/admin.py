from django.contrib import admin
from .models import Trip

admin.site.register(Trip)
admin.site.site_header = 'Travelly Administration'
