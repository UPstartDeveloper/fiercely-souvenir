from django.db import models
from django.contrib.auth.models import User


class Airline(models.Model):
    '''Represents a company that Users fly with.'''
    pass


class Review(models.Model):
    '''Feedback a User has about their experience with a certain airline.'''
    pass
