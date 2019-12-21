from django.urls import path
from trips.views import (
    show_trips,
    show_airlines
)

app_name = 'trips'
urlpatterns = [
    path('trips/', show_trips, name="all-trips"),
    path('airlines/', show_airlines, name="all-airlines"),
]
