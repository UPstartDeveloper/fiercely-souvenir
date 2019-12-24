from django.urls import path
from trips.views import (
    TripList,
)

app_name = 'trips'
urlpatterns = [
    path('trips/', TripList.as_view(), name="all-trips"),
]
