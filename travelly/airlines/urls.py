from django.urls import path
from airlines.views import (
    AirlineList,
    AirlineDetail,
    AirlineCreate
)

app_name = 'airlines'
urlpatterns = [
    path('all/', AirlineList.as_view(), name="all-airlines"),
    path('add-airline/', AirlineCreate.as_view(), name='create_airline'),
    path('<slug:slug>/reviews/', AirlineDetail.as_view(),
         name='airline-detail'),
]
