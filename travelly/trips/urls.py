from django.urls import path
from trips.views import (
    TripList,
    TripDetail
)

app_name = 'trips'
urlpatterns = [
    path('trips/', TripList.as_view(), name="all-trips"),
    path('<slug:slug>/', TripDetail.as_view(), name="trip-detail"),
]
