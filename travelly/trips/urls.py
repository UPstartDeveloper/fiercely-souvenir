from django.urls import path
from trips.views import (
    TripList,
    TripDetail,
    TripCreate
)

app_name = 'trips'
urlpatterns = [
    path('trips/', TripList.as_view(), name="all-trips"),
    path('create-trip/', TripCreate.as_view(), name="create-trip"),
    path('<int:pk>/', TripDetail.as_view(), name="trip-detail"),
]
