from django.urls import path
from airlines.views import (
    AirlineList,
)

app_name = 'airlines'
urlpatterns = [
    path('all/', AirlineList.as_view(), name="all-airlines"),
]
