from django.urls import path
from airports.views import (
    AirportList,
    AirportCreate,
)

app_name = 'airports'
urlpatterns = [
    path('options/', AirportList.as_view(), name="home"),
    path('add-airport/', AirportCreate.as_view(), name="add_airport"),
]
