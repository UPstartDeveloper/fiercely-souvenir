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
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Abdullah',
                                        email='abd@gmail.com',
                                        password="Abdullah's passwd")
        self.airline = Airline.objects.create(title='Summer Break',
                                              verified=True)
        self.airline_url = 'airlines:create_airline'
        self.review_url = 'airlines:create_review'

    def test_get_create_airline_form(self):
        '''User requests to see the form to add a new airline.'''
        # user is already logged in, so they pass the LoginRequiredMixin
        self.assertTrue(self.user.is_authenticated)
        # user makes a GET request to AirlineCreate view
        get_request = self.factory.get(self.airline_url)
        get_request.user = self.user
        # user gets a valid response from the server
        response = AirlineCreate.as_view()(get_request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Got an Airline to Share?')

    def test_get_create_review_form(self):
        '''User requests to see the form to add a review.'''
        # user is already logged in, so they pass the LoginRequiredMixin
        self.assertTrue(self.user.is_authenticated)
        # user makes a GET request to AirlineCreate view
        get_request = self.factory.get(self.review_url)
        get_request.user = self.user
        # user gets a valid response from the server
        response = ReviewCreate.as_view()(get_request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Have an Experience to Share?')

    def test_insert_airline(self):
        '''User adds an airline to the database.'''
        # user is already logged in, so they pass the LoginRequiredMixin
        self.assertTrue(self.user.is_authenticated)
        # user fills out the form on the AirlineCreate page
        title_for_airline = 'United Airlines'
        form_data = {
            'title': title_for_airline,
        }
        # user submits the form
        post_request = self.factory.post(self.airline_url, form_data)
        post_request.user = self.user
        response = AirlineCreate.as_view()(post_request)
        # the new airline object exists, and is NOT verified by default
        new_airline = Airline.objects.get(title=title_for_airline)
        self.assertTrue(new_airline, not None)
        self.assertEqual(new_airline.verified, False)
        # user is redirected
        self.assertEqual(response.status_code, 302)

    def test_insert_review(self):
        '''User adds a review for an airline.'''
        # user is already logged in, so they pass the LoginRequiredMixin
        self.assertTrue(self.user.is_authenticated)
        # an airline already exists in the database
        airline = Airline.objects.get(title=self.airline.title)
        self.assertTrue(airline, not None)
        # user fills out form to create a reivew
        review_headline = 'Great Service!'
        form_data = {
            'airline': airline,
            'headline': review_headline,
            'rating': 5,
            'comments': 'Highly Recommended!',
            'price': 67.87,
        }
        # user submits the form
        post_request = self.factory.post(self.review_url, form_data)
        post_request.user = self.user
        response = ReviewCreate.as_view()(post_request)
        self.assertEqual(response.status_code, 302)
        # a new Review instance is in the db
        # new_review = Review.objects.get(headline=review_headline)
        # self.assertTrue(new_review, not None)
        # user is redirected
        # self.assertEqual(response.status_code, 302)


class AirlineListTests(TestCase):
    '''The user sees all the Airlines that are in the database.'''
    def setUp(self):
        """Instantiate the Users, Airline, Review, and RequestFactory instances
           needed for testing.

        """
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Abdullah',
                                        email='abd@gmail.com',
                                        password="Abdullah's passwd")
        self.airline = Airline.objects.create(title='United Airlines',
                                              verified=True)
        self.review = Review.objects.create(airline=self.airline,
                                            headline='Great Service!',
                                            rating=5,
                                            comments='Highly Recommended!',
                                            price=697.87)


class AirlineAndReviewDetailTests(TestCase):
    '''User sees both details about the airline, and its reviews.'''
    def setUp(self):
        """Instantiate the Users, Airline, Review, and RequestFactory instances
           needed for testing.

        """
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Abdullah',
                                        email='abd@gmail.com',
                                        password="Abdullah's passwd")
        self.airline = Airline.objects.create(title='United Airlines',
                                              verified=True)
        self.review = Review.objects.create(airline=self.airline,
                                            headline='Great Service!',
                                            rating=5,
                                            comments='Highly Recommended!',
                                            price=697.87)

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
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Abdullah',
                                        email='abd@gmail.com',
                                        password="Abdullah's passwd")
        self.airline = Airline.objects.create(title='United Airlines',
                                              verified=True)
        self.review = Review.objects.create(airline=self.airline,
                                            headline='Great Service!',
                                            rating=5,
                                            comments='Highly Recommended!',
                                            price=697.87)


class ReviewDeleteTests(TestCase):
    '''User deletes their own review posts if they please.'''
    def setUp(self):
        """Instantiate the Users, Airline, Review, and RequestFactory instances
           needed for testing.

        """
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Abdullah',
                                        email='abd@gmail.com',
                                        password="Abdullah's passwd")
        self.review = Review.objects.create(airline=self.airline,
                                            headline='Great Service!',
                                            rating=5,
                                            comments='Highly Recommended!',
                                            price=697.87)
