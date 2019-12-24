from django.db import models
from django.contrib.auth.models import User
from airlines.models import Airline
from travelly import settings
from django.utils.text import slugify
from django.utils import timezone


class Trip(models.Model):
    '''A journey taken by a User.'''
    title = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                             unique=True,
                             help_text="A memorable title for your trip.")
    slug = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                            blank=True, editable=False,
                            help_text="Unique URL path to access this note." +
                                      "Computer Generated.")
    passenger = models.ForeignKey(User, null=True, on_delete=models.PROTECT,
                                  help_text="The user making this journey.")
    arrive_at = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                                 blank=True, editable=True)
    SFO_GATES = (
        ('G', 'International Terminal G'),
        ('A', 'International Terminal A'),
        ('2D', 'Terminal 2'),
        ('1B', 'Harvey Milk Terminal 1B'),
        ('1C', 'Harvey Milk Terminal 1C'),
        ('3', 'Terminal 3'),
    )
    terminal = models.CharField(max_length=2, choices=SFO_GATES,
                                help_text=(
                                    "Check " +
                                    "https://www.flysfo.com/flight-info/airlines-at-sfo " +
                                    "to see which Terminal you need to check" +
                                    " in at for your flight."
                                ))
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

    def instruct(self):
        '''Display info on what the user must do to undertake this Trip.'''
        return (
            '1. Arrive at SFO International. ' +
            'For novice fliers, I recommend arriving at least 3 hours before' +
            " the time your flight is scheduled to start boarding " +
            "('Boarding Time'). " +
            f'2. Check-in time! Please locate {self.terminal}, so that you ' +
            f'can talk to the nice people at your airline '
            + f'who will clear your boarding pass, and assess your luggage' +
            'for any bags that need to be checked in. ' +
            "3. Go through security! Don't sweat this part: take a deep " +
            'breath, be patient, and be sure to review the guidelines on ' +
            'https://www.tsa.gov/travel/security-screening/whatcanibring/all' +
            ' before your day at the airport! ' +
            "4. You're almost to the plane! Please check your boarding pass to"
            " see which gate you will need to wait at, until it's boarding " +
            "time. " +
            "5. Get on the plane! " +
            "6. Enjoy the ride! Watch movies, read a book, nap, or have a " +
            'bizarre conversation with the person sitting next to you... ' +
            f"7. When you reach your destination at {self.arrive_at}, you " +
            'be able to get off the plane. Congratulations on making the trip!'
        )
