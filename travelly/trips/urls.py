from django.urls import path
from trips.views import (
    hello_world
)

app_name = 'trips'
urlpatterns = [
    path('trips/', hello_world, name="all-trips"),
]
