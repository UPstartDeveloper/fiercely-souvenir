from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from trips.models import Trip
from django.urls import reverse, reverse_lazy
from trips.views import (
    TripList, TripDetail, TripCreate, TripUpdate, TripDelete
)


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
        request = self.factory.get('trips:all-trips')
        response = TripList.as_view()(request)
        self.assertEqual(response.status_code, 200)
        # ensure that the user sees the content from the specific Trip instance
        self.assertContains(response, 'Summer Break')


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

    def test_get_create_form(self):
        '''The site has a form a user can see to make new Trip instances.'''
        # use makes a request to GET the create form
        get_request = self.factory.get('trips:create-trip')
        response = TripCreate.as_view()(get_request)
        # the page renders with the correct content on the template
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Going Somewhere?')

    def test_insert_one_trip_in_db(self):
        '''A Trip instance created by a User goes in the database.'''
        # user passes in data through the TripCreate form
        form_data = {
            'title': "Summer Break",
            'arrive_at': "BOS",
            'terminal': 'G'
        }
        post_request = self.factory.post('trips:create-trip', form_data)
        post_request.user = self.user  # the user becomes the passenger
        # the Trip is inserted into the database
        response = TripCreate.as_view()(post_request)
        # a new Trip instance exists, with the content the user inputted
        new_trip = Trip.objects.get(title='Summer Break')
        self.assertTrue(new_trip, not None)
        # the user is redirected
        self.assertEqual(response.status_code, 302)


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
