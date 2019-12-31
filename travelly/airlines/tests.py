from django.test import TestCase
from airlines.views import (
    AirlineList,
    AirlineDetail,
    AirlineCreate,
    AirlineUpdate,
    ReviewCreate,
    ReviewUpdate,
    ReviewDelete
)
from airlines.models import Airline, Review
