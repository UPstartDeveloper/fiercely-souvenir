from django.test import TestCase


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
    pass


class TripDetailTests(TestCase):
    '''Tests for the TripDetail view.'''
    pass


class TripUpdateTests(TestCase):
    '''Tests for the TripUpdate view.'''
    pass


class TripDeleteTests(TestCase):
    '''Tests for the TripDelete view.'''
    pass
