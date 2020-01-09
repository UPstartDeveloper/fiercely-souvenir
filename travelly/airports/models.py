from django.db import models
from travelly.settings import ADDRESS_MAX_LENGTH
from django.conf import settings


class AirportAddress(models.Model):
    '''The address of the airport the User is at.'''
    title = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                             unique=True,
                             help_text="A memorable title for your trip.")
    slug = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                            blank=True, editable=False,
                            help_text="Unique URL path to access this trip." +
                                      "Computer Generated.")
    address = models.CharField(max_length=ADDRESS_MAX_LENGTH,
                               blank=True, editable=True, help_text=(
                                      "What's the full address of the airport?"
                                      ))

    def __str__(self):
        '''Return the title of the AirportAddress for presentation purposes.'''
        return self.title

    def get_absolute_url(self):
        '''Returns a fully qualified path for an airport.'''
        pass

    def save(self, *args, **kwargs):
        '''Creates a URL safe slug automatically when a new airport is made.'''
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # call save on the superclass
        return super(AirportAddress, self).save(*args, **kwargs)
