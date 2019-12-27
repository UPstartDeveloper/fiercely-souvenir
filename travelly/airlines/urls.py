from django.urls import path
from airlines.views import (
    AirlineList,
    AirlineDetail,
    AirlineCreate,
    AirlineUpdate,
    ReviewCreate,
)

app_name = 'airlines'
urlpatterns = [
    # Airline views
    path('all/', AirlineList.as_view(), name="all-airlines"),
    path('add-airline/', AirlineCreate.as_view(), name='create_airline'),
    path('<slug:slug>/reviews/', AirlineDetail.as_view(),
         name='airline-detail'),
    path('<slug:slug>/edit-airline-details/', AirlineUpdate.as_view(),
         name="update_airline"),
    # Review views
    path('add-review/', ReviewCreate.as_view(), name='create_review'),
]
