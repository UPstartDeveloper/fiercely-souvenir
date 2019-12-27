from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    '''Comments that users have about their flying experience.'''
    airline = models.ForeignKey('Airline', on_delete=models.PROTECT)
    comments = ''  # charfield


class Rating(models.Model):
    '''A 1-5 star (5 is exceptional, 1 is terrible) rating of the airline.'''
    airline = models.ForeignKey('Airline', on_delete=models.PROTECT)
    stars = ''  # integer


class Cost(models.Model):
    '''The price paid to fly with an airline, by a user.'''
    airline = models.ForeignKey('Airline', on_delete=models.PROTECT)
    price = None  # decimal or flaotfield


class Airline(models.Model):
    '''Provides User with flying services.'''
    passengers = models.ManyToManyField(User)
