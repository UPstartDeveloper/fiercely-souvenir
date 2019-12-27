from django.urls import path
from airlines.views import (
    AirlineList,
    AirlineDetail,
)

app_name = 'airlines'
urlpatterns = [
    path('all/', AirlineList.as_view(), name="all-airlines"),
    path('<slug:slug>/reviews/', AirlineDetail.as_view(),
         name='airline-detail'),
]
