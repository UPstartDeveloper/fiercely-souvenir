from django.urls import path
from trips.views import (
    TripList,
    TripDetail,
    TripCreate,
    TripUpdate,
    TripDelete
)

app_name = 'trips'
urlpatterns = [
    path('trips/', TripList.as_view(), name="all-trips"),
    path('create-trip/', TripCreate.as_view(), name="create-trip"),
    path('<int:pk>/', TripDetail.as_view(), name="trip-detail"),
    path('<int:pk>/change-details', TripUpdate.as_view(), name='change-trip'),
    path('<int:pk>/delete-trip', TripDelete.as_view(), name='delete-trip'),
]
