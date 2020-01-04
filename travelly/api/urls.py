from django.urls import path
import api.views as api_views

app_name = 'api'
urlpatterns = [
    # Trips model API
    path('trips/', api_views.TripListOrCreate.as_view(), name='all-trips'),
    path('trips/<int:pk>/', api_views.TripReadUpdateOrDelete.as_view(),
         name='trip-rud'),
    # Airline model API
    path('airlines/', api_views.AirlineListOrCreate.as_view(),
         name='all-airlines'),
    path('airlines/<int:pk>/', api_views.AirlineReadUpdateOrDelete.as_view(),
         name='airline-rud'),
    # Review model API
    path('reviews/', api_views.ReviewListOrCreate.as_view(),
         name='all-reviews'),
    path('reviews/<int:pk>/', api_views.ReviewReadUpdateOrDelete.as_view(),
         name='review-rud'),
]
