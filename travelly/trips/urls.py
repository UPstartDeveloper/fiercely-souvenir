from django.urls import path
from trips.views import (
    show_trips,
)

app_name = 'trips'
urlpatterns = [
    path('trips/', show_trips, name="all-trips"),
]
