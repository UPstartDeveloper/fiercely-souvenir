from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from trips.models import Trip
from django.contrib.auth.models import User
from trips.forms import TripForm


class TripList(ListView):
    '''Renders all the Trips currently made by site Users.'''
    model = Trip
    template_name = 'trips/index.html'

    def get(self, request):
        '''Render a context containing all Trip instances.'''
        trips = self.get_queryset().all()
        return render(request, self.template_name, {
            'trips': trips
        })


class TripDetail(DetailView):
    '''Displays a page with instructions associated with a specific trip.'''
    model = Trip
    template_name = 'trips/instructions.html'

    def get(self, request, slug):
        """Renders a page to show the boarding instructions for a single Trip.

           Parameters:
           request(HttpRequest): the GET request sent to the server
           slug(slug): unique slug field value of the Trip instance

           Returns:
           HttpResponse: the view of the detail template

        """
        trip = self.get_queryset().get(slug__iexact=slug)
        context = {
            'trip': trip
        }
        return render(request, self.template_name, context)
