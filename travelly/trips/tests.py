from django.test import TestCase


class TripsTestCase(TestCase):
    def test_true_is_true(self):
        '''Canary test to make sure environment is working correctly.'''
        self.assertEqual(True, True)
        self.assertEqual(True, False, (
            'You are able to throw errors correctly.'
        ))
