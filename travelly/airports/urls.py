from django.urls import path
from airports.views import show_options

app_name = 'airports'
urlpatterns = [
    path('options/', show_options, name="home"),
]
