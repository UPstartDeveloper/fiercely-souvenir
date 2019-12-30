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
        """Instantiate RequestFactory, Trip, and User objects to pass requests
           to the TripList view.

           Parameters:
           self(TripListTests): the calling object

           Returns:
           None

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

           Parameters:
           self(TripCreateTests): the calling object

           Returns:
           None

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
    def setUp(self):
        """Instantiate RequestFactory, Trip, and User objects to pass requests
           to the TripDetail view.

           Parameters:
           self(TripDetailTests): the calling object

           Returns:
           None

        """
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Abdullah',
                                        email='abd@gmail.com',
                                        password="Abdullah's passwd")
        self.trip = Trip.objects.create(title="Summer Break",
                                        passenger=self.user, arrive_at="BOS",
                                        terminal='G')

    def test_get_details_for_one_trip(self):
        '''A user sees instructions for a Trip on its details page.'''
        # a user makes a request to see the page
        self.assertEqual(self.trip.id, 2)
        get_request = self.factory.get('trips/2/')
        # the page renders ok
        response = TripDetail.as_view()(get_request, self.trip.id)
        self.assertEqual(response.status_code, 200)
        # the page renders the instructions ok
        instruction = f'your destination at: {self.trip.arrive_at}'
        self.assertContains(response, instruction)


class TripUpdateTests(TestCase):
    '''Tests for the TripUpdate view.'''
    def setUp(self):
        """Instantiate RequestFactory and User objects to pass POST requests
           to the TripUpdate view.

           Parameters:
           self(TripUpdateTests): the calling object

           Returns:
           None

        """
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Abdullah',
                                        email='abd@gmail.com',
                                        password="Abdullah's passwd")
        self.trip = Trip.objects.create(title="Summer Break",
                                        passenger=self.user, arrive_at="BOS",
                                        terminal='G')
        self.url = 'trips/4/change-details/'

    def pass_test_func(self, user):
        """Check to make sure the request meets the requirements of the
           UserPassesTestMixin that TripUpdate inherits from.

           Parameters:
           user(User): the client making the request

           Returns
           bool: True or False, depending on whether the client is the Trip
                 passenger

        """
        return self.trip.passenger == user

    def test_changing_trip_fields(self):
        """A user is able to change the title, arrive_at, or terminal fields
            of a pre-exisiting Trip.

        """
        # there is already a Trip in the db
        old_trip = Trip.objects.get(title=self.trip.title)
        self.assertTrue(old_trip, not None)
        # the user is able to GET the update from
        self.assertEqual(self.trip.id, 4)
        get_request = self.factory.get(self.url)
        # the user making this request passes the UserPassesTestMixin of view
        self.assertTrue(True, self.pass_test_func(self.user))
        get_request.user = self.user
        response = TripUpdate.as_view()(get_request, pk=self.trip.id)
        self.assertEqual(response.status_code, 200)
        # the user can then POST changes to the database
        new_title = 'End of School-Year Journeys'
        form_data = {
            'title': new_title,
            'arrive_at': 'OAK',
            'terminal': 'A'
        }
        post_request = self.factory.post(self.url, form_data)
        # the user making this request passes the UserPassesTestMixin of view
        self.assertTrue(True, self.pass_test_func(self.user))
        post_request.user = self.user
        response = TripUpdate.as_view()(post_request, form_data, pk=self.trip.id)
        # the user is then redirected
        self.assertEqual(response.status_code, 302)
        # the Trip fields have been chnaged to match the user data
        new_trip = Trip.objects.get(title=new_title)
        self.assertTrue(new_trip, not None)


class TripDeleteTests(TestCase):
    '''Tests for the TripDelete view.'''
    def setUp(self):
        """Instantiate RequestFactory and User objects to pass POST requests
           to the TripDelete view.

           Parameters:
           self(TripDeleteTests): the calling object

           Returns:
           None

        """
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Abdullah',
                                        email='abd@gmail.com',
                                        password="Abdullah's passwd")
