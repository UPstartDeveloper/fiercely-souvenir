from django.db import models


class Address(models.Model):
    '''The address of the airport the User is at.'''
    pass


class HotelSearch(models.Model, Address):
    '''Represents a search a User makes for nearby hotels at an airport.'''
    pass


class CarRentalSearch(models.Model, Address):
    '''Represents a search a User makes for nearby hotels at an airport.'''
    pass
