from django.db import models
from travelly.settings import AUTH_USER_MODEL as User
from airlines.models import Airline
from travelly import settings


# Create your models here.
class Trip(models.Model):
    '''A journey taken by a User.'''
    title = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                             unique=True,
                             help_text="A memorable title for your trip.")
    slug = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                            blank=True, editable=False,
                            help_text="Unique URL path to access this note." +
                                      "Computer Generated.")
    departure_airport = '' # Airport
    arrival_airport = ''  # Airport
    passenger = models.ForeignKey(User, null=True, on_delete=models.PROTECT,
                                  help_text="The user making this journey.")
    gate_of_entry = '' # based off airline and departure_airport
    gate_of_exit = ''  # based off airline and arrival_airport
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this note " +
                                   "was created. Auto-generated.")

    def __str__(self):
        '''Return the title of the Trip for presentation purposes.'''
        return self.title

    def get_absolute_url(self):
        '''Returns a fully qualified path for a page (i.e. /my-note).'''
        path_components = {'slug': self.slug}
        return reverse('notes:notes-detail-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        '''Creates a URL safe slug automatically when a new note is saved.'''
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # call save on the superclass
        return super(Trip, self).save(*args, **kwargs)


class Airport(models.Model):
    '''The place a User can depart from or arrive upon.'''
    pass
