from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from trips.models import Trip
from airlines.models import Airline, Review
from api.serializers import TripSerializer, AirlineSerializer, ReviewSerializer


class TripListOrCreate(ListCreateAPIView):
    """Presents a list of all Trip instances.
       Allows for the creation of single Trip.
       Method handlers for GET and POST.

    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class TripReadUpdateOrDelete(RetrieveUpdateDestroyAPIView):
    """User is able to read, update, or delete a Trip instance.
       Lookup uses the id field of the specific Trip object.
        Work with GET, PUT, PATCH, or DELETE methods.

    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class AirlineListOrCreate(ListCreateAPIView):
    """Presents a list of all Airline instances.
       Allows for the creation of single Airline.
       Method handlers for GET and POST.

    """
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer


class AirlineReadUpdateOrDelete(RetrieveUpdateDestroyAPIView):
    """User is able to read, update, or delete a Airline instance.
       Lookup uses the id field of the specific Airline object.
        Work with GET, PUT, PATCH, or DELETE methods.

    """
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer


class ReviewListOrCreate(ListCreateAPIView):
    """Presents a list of all Review instances.
       Allows for the creation of single Review.
       Method handlers for GET and POST.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewReadUpdateOrDelete(RetrieveUpdateDestroyAPIView):
    """User is able to read, update, or delete a Review instance.
       Lookup uses the id field of the specific Review object.
        Work with GET, PUT, PATCH, or DELETE methods.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
