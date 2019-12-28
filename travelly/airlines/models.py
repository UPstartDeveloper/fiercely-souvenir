from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy


class Airline(models.Model):
    '''Represents a company that Users fly with.'''
    title = models.CharField(max_length=200, help_text="Name of this airline.",
                             unique=True)
    slug = models.CharField(max_length=200,
                            blank=True, editable=False,
                            help_text="Unique URL path to access this airline."
                                      + "Computer Generated.")
    logo = models.ImageField(upload_to='images/',
                             default='images/air-transport.png',
                             help_text="Brand image of the airline.")
    verified = models.BooleanField(help_text="Staff-checked for credibility.")

    def __str__(self):
        '''Return the title of the Airline for presentation purposes.'''
        return self.title

    def get_absolute_url(self):
        '''Returns a fully qualified path for a page (i.e. /delta-airlines).'''
        path_components = {'slug': self.slug}
        return reverse('airlines:airline-detail', kwargs=path_components)

    def save(self, *args, **kwargs):
        '''Makes a URL safe slug automatically when a new instance is saved.'''
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # call save on the superclass
        return super(Airline, self).save(*args, **kwargs)


class Review(models.Model):
    '''Feedback a User has about their experience with a certain airline.'''
    headline = models.CharField(max_length=200,
                                help_text="Headline for review.",
                                unique=False)
    author = models.OneToOneField(User, null=True,
                                  on_delete=models.SET_NULL)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
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
    price = models.DecimalField(max_digits=9, decimal_places=2,
                                help_text=(
                                    "How much did you pay this airline? " +
                                    "Please leave out currency symbols " +
                                    "(i.e. $)."
                                ))
    comments = models.TextField(help_text=(
        "What was your experience like? All feedback is encouraged!"))

    def __str__(self):
        '''Return the title of the Review for presentation purposes.'''
        return f"{self.airline} Review {self.id}"

    def get_absolute_url(self):
        '''Returns a fully qualified path for related AirlineDetail page.'''
        path_components = {'slug': self.airline.slug}
        return reverse('airlines:airline-detail', kwargs=path_components)
