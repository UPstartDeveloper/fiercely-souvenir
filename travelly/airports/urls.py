from django.urls import path
from airports.views import (
    AirportList,
)

app_name = 'airports'
urlpatterns = [
    path('options/', AirportList.as_view(), name="home"),
]
