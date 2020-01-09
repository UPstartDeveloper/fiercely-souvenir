from django.urls import path
from airports.views import (
    AirportList,
    AirportCreate,
    AirportDetail,
    AirportUpdate,
    AirportDelete
)

app_name = 'airports'
urlpatterns = [
    path('options/', AirportList.as_view(), name="home"),
    path('add-airport/', AirportCreate.as_view(), name="add_airport"),
    path('<slug:slug>/change-airport/', AirportUpdate.as_view(),
         name='edit_airport'),
    path('<slug:slug>/delete-airport/', AirportDelete.as_view(),
         name='delete_airport'),
    path('<slug:slug>/', AirportDetail.as_view(), name="airport_details"),
]
