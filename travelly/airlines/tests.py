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
from django.test.client import RequestFactory


class AirlineAndReviewCreateTests(TestCase):
    '''Users add Airline and Review objects to the database.'''
    def setUp(self):
        """Instantiate the Users, Airline, Review, and RequestFactory instances
           needed for testing.

        """
        pass

    def test_get_create_airline_form(self):
        '''User requests to see the form to add a new airline.'''
        pass

    def test_get_create_review_form(self):
        '''User requests to see the form to add a review.'''
        pass

    def test_insert_airline(self):
        '''User adds an airline to the database.'''
        pass

    def test_insert_review(self):
        '''User adds a review for an airline.'''
        pass


class AirlineListTests(TestCase):
    '''The user sees all the Airlines that are in the database.'''
    def setUp(self):
        """Instantiate the Users, Airline, Review, and RequestFactory instances
           needed for testing.

        """
        pass


class AirlineAndReviewDetailTests(TestCase):
    '''User sees both details about the airline, and its reviews.'''
    def setUp(self):
        """Instantiate the Users, Airline, Review, and RequestFactory instances
           needed for testing.

        """
        pass

    def test_see_airline_after_user_deletion(self):
        """An airline is still visibile after the user who posted it is deleted
           from the database.

        """
        pass

    def test_see_review_after_user_deletion(self):
        """A reivew is still visibile after the user who posted it is deleted
           from the database.

        """
        pass


class AirlineAndReviewUpdateTests(TestCase):
    '''Users who post about airlines or reviews arw able to edit their post.'''
    def setUp(self):
        """Instantiate the Users, Airline, Review, and RequestFactory instances
           needed for testing.

        """
        pass


class ReviewDeleteTests(TestCase):
    '''User deletes their own review posts if they please.'''
    def setUp(self):
        """Instantiate the Users, Airline, Review, and RequestFactory instances
           needed for testing.

        """
        pass
