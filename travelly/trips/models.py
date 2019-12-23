from django.db import models
from django.contrib.auth.models import User
from airlines.models import Airline
from travelly import settings


class Airport(models.Model):
    '''The place a User can depart from or arrive upon.'''
    pass


class Trip(models.Model):
    '''A journey taken by a User.'''
    title = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                             unique=True,
                             help_text="A memorable title for your trip.")
    slug = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                            blank=True, editable=False,
                            help_text="Unique URL path to access this note." +
                                      "Computer Generated.")
    arrival_airport = models.OneToOneField(Airport, on_delete=models.PROTECT,
                                           primary_key=False)
    passenger = models.ForeignKey(User, null=True, on_delete=models.PROTECT,
                                  help_text="The user making this journey.")
    gate_of_entry = ''
    gate_of_exit = ''
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
