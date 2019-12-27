from django.db import models
from django.contrib.auth.models import User


class Airline(models.Model):
    '''Represents a company that Users fly with.'''
    name = models.CharField(max_length=200, help_text="Name of this airline.",
                            unique=True)
    slug = models.CharField(max_length=200,
                            blank=True, editable=False,
                            help_text="Unique URL path to access this airline."
                                      + "Computer Generated.")
    logo = models.ImageField(upload_to='images/',
                             default='images/air-transport.png',
                             help_text="Brand image of the airline.")
    verified = models.BooleanField(help_text="Staff-checked for credibility.")


class Review(models.Model):
    '''Feedback a User has about their experience with a certain airline.'''
    author = = models.OneToOneField(settings.AUTH_USER_MODEL,
                                    on_delete=models.SET_NULL)
    airline = models.ForeignKey(Airline, on_delete=models.DELETE)
    RATING_CHOICES = [
        (1, 'One Star'),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Stars'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES, help_text=(
        "On a scale from 1-5, with 1 meaning 'terrible' and 5 meaning " +
        "'exceptional', how would you rate your experience with this airline?"
    ))
    price = models.DecimalField(decimal_places=2,
                                help_text="How much did you pay this airline?")
    comments = models.TextField(help_text=(
        "What was your experience like? All feedback is encouraged!"))
