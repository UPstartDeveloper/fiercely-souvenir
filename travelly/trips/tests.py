from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from trips.models import Trip
from django.urls import reverse, reverse_lazy
import trips.views as trips_views


class TripsTestCase(TestCase):
    def test_true_is_true(self):
        '''Canary test to make sure environment is working correctly.'''
        self.assertEqual(True, True)
        """
        self.assertEqual(True, False, (
            'You are able to throw errors correctly.'
        ))
        """


class TripListTests(TestCase):
    '''Tests for the TripList view.'''
    def setUp(self):
        """Instantiate RequestFactory and User objects to pass POST requests
           to the TripCreate view.

        """
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Abdullah',
                                        email='abd@gmail.com',
                                        password="Abdullah's passwd")
        self.trip = Trip.objects.create(title="Summer Break",
                                        passenger=self.user, arrive_at="BOS",
                                        terminal='G')

    def test_get_list_page(self):
        '''A user is able to see all the Trips in the database on the list.'''
        # add Trip objects to the database
        self.trip.save()
        # make sure that the trip is shown on the TripList view
        get_request = self.factory.get('trips:all-trips')
        response = trips_views.TripList.as_view()(get_request)
        self.assertEqual(response.status_code, 200)


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
