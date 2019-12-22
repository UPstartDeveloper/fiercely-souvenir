from django.urls import path
from airlines.views import (
    show_airlines,
)

app_name = 'airlines'
urlpatterns = [
    path('all/', show_airlines, name="all-airlines"),
]
