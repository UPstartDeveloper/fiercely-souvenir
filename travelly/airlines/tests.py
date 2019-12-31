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
from django.contrib.auth.models import User


class AirlineAndReviewCreateTests(TestCase):
    '''Users add Airline and Review objects to the database.'''
    pass


class AirlineListTests(TestCase):
    '''The user sees all the Airlines that are in the database.'''
    pass


class AirlineDetailTests(TestCase):
    '''User sees both details about the airline, and its reviews.'''
    pass


class AirlineAndReviewUpdateTests(TestCase):
    '''Users who post about airlines or reviews arw able to edit their post.'''
    pass


class ReviewDeleteTests(TestCase):
    '''User deletes their own review posts if they please.'''
    pass
