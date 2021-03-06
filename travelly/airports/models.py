from django.db import models
from travelly.settings import ADDRESS_MAX_LENGTH
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy
import googlemaps
from travelly.settings import GMAPS_KEY


class AirportAddress(models.Model):
    '''The address of the airport the User is at.'''
    title = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                             unique=True,
                             help_text=(
                                "For best results, please enter an IATA " +
                                "airport code, or the full name of the " +
                                "airport."
                             ))
    slug = models.CharField(max_length=settings.FLIGHT_TITLE_MAX_LENGTH,
                            blank=True, editable=False,
                            help_text="Unique URL path to access this trip." +
                                      "Computer Generated.")
    location = models.CharField(max_length=ADDRESS_MAX_LENGTH,
                                blank=True, editable=True, help_text=(
                                      "What's the full address of the airport?"
                                      ))

    def __str__(self):
        '''Return the title of the AirportAddress for presentation purposes.'''
        return self.title

    def get_absolute_url(self):
        '''Returns a fully qualified path for an airport.'''
        path_components = {'slug': self.slug}
        return reverse('airports:airport_details', kwargs=path_components)

    def get_coordinates(self):
        '''Return the geographical coordinates of an AirportAddress.'''
        # make the gmaps client
        gmaps = googlemaps.Client(key=GMAPS_KEY)
        # get the address of the airport using Google maps api
        address = gmaps.places(self.title)
        # convert the address into latitude and longitude using Geocoding API
        coordinates = address['results'][0]['geometry']['location']
        lat_long = (coordinates['lat'], coordinates['lng'])
        # return the coordinates
        return lat_long

    def get_nearby_hotels(self, lat_long):
        """Given the coordinates of this address, return nearby hotels using
           the Google Maps Places API.

        """
        # make the google maps client
        gmaps = googlemaps.Client(key=GMAPS_KEY)
        # send a request for nearby hotels to the API
        search = f'hotels near {self.title}'
        places_result = gmaps.places(query=('hotel near ' + self.title))
        # return the names and addresses of the hotels
        hotels = places_result.get("results")
        addr = "formatted_address"  # a key to grab from API respomse
        hotels_and_addresses = [
            (hotel.get("name"), hotel.get(addr)) for hotel in hotels
        ]
        return hotels_and_addresses

    def save(self, *args, **kwargs):
        '''Creates a URL safe slug automatically when a new airport is made.'''
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # call save on the superclass
        return super(AirportAddress, self).save(*args, **kwargs)
