from django.db import models
from django.contrib.auth.models import User
from airlines.models import Airline
from travelly import settings
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse, reverse_lazy


class Trip(models.Model):
    '''A journey taken by a User.'''
    title = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                             unique=True,
                             help_text="A memorable title for your trip.")
    slug = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                            blank=True, editable=False,
                            help_text="Unique URL path to access this trip." +
                                      "Computer Generated.")
    passenger = models.ForeignKey(User, null=True, on_delete=models.PROTECT,
                                  help_text="The user making this journey.")
    airline = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                               blank=True, editable=True, help_text=(
                                      "Which airline are you flying with?"))
    depart_from = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                                   blank=True, editable=True, help_text=(
                                      "Which airport are you boarding from?"
                                    ))
    arrive_at = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                                 blank=True, editable=True, help_text=(
                                    "Which airport are you flying to?"
                                 ))
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this note " +
                                   "was created. Auto-generated.")

    def __str__(self):
        '''Return the title of the Trip for presentation purposes.'''
        return self.title

    def get_absolute_url(self):
        '''Returns a fully qualified path for a trip.'''
        path_components = {'pk': self.pk}
        return reverse('trips:trip-detail', kwargs=path_components)

    def save(self, *args, **kwargs):
        '''Creates a URL safe slug automatically when a new note is saved.'''
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # call save on the superclass
        return super(Trip, self).save(*args, **kwargs)
