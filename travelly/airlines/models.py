from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    '''Comments that users have about their flying experience.'''
    pass


class Rating(models.Model):
    '''A 1-5 star (5 is exceptional, 1 is terrible) rating of the airline.'''


class Cost(models.Model):
    '''The price paid to fly with an airline, by a user.'''
    pass


class Airline(models.Model):
    '''Provides User with flying services.'''
    passengers = models.ManyToManyField(User, on_delete=models.PROTECT)
