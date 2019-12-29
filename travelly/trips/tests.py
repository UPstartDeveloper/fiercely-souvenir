from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from trips.models import Trip
from django.urls import reverse, reverse_lazy


class TripsTestCase(TestCase):
    def test_true_is_true(self):
        '''Canary test to make sure environment is working correctly.'''
        self.assertEqual(True, True)
        """
        self.assertEqual(True, False, (
            'You are able to throw errors correctly.'
        ))
        """


class TripCreateTests(TestCase):
    '''Tests for the TripCreate view.'''
    def setUp(self):
        """Instantiate RequestFactory and User objects to pass POST requests
           to the TripCreate view.

        """
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Abdullah',
                                        email='abd@gmail.com',
                                        password="Abdullah's passwd")


class TripDetailTests(TestCase):
    '''Tests for the TripDetail view.'''
    pass


class TripUpdateTests(TestCase):
    '''Tests for the TripUpdate view.'''
    def setUp(self):
        """Instantiate RequestFactory and User objects to pass POST requests
           to the TripUpdate view.

        """
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Abdullah',
                                        email='abd@gmail.com',
                                        password="Abdullah's passwd")


class TripDeleteTests(TestCase):
    '''Tests for the TripDelete view.'''
    def setUp(self):
        """Instantiate RequestFactory and User objects to pass POST requests
           to the TripDelete view.

        """
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Abdullah',
                                        email='abd@gmail.com',
                                        password="Abdullah's passwd")
