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

    def get(self, request, pk):
        """Renders a page to show the boarding instructions for a single Trip.

           Parameters:
           request(HttpRequest): the GET request sent to the server
           slug(slug): unique slug field value of the Trip instance

           Returns:
           HttpResponse: the view of the detail template

        """
        trip = self.get_queryset().get(pk=pk)
        context = {
            'trip': trip
        }
        return render(request, self.template_name, context)


class TripCreate(CreateView):
    '''Allows user to add new Trip instances.'''
    model = Trip
    form_class = TripForm
    template_name = 'trips/create.html'
    queryset = Trip.objects.all()

    def form_valid(self, form):
        '''Initializes the passenger based on who submitted the form.'''
        form.instance.passenger = self.request.user
        return super().form_valid(form)


class TripUpdate(UpdateView):
    '''Allows for editing of a trip.'''
    model = Trip
    form_class = TripForm
    template_name = 'trips/update.html'
    queryset = Trip.objects.all()


class TripDelete(DeleteView):
    '''Allows for removal of Trip instances by User.'''
    model = Trip
    template_name = 'trips/deletion.html'
    success_url = reverse_lazy('trips:all-trips')
    queryset = Trip.objects.all()

    def get(self, request, pk):
        """Renders a page to show the boarding instructions for a single Trip.

           Parameters:
           request(HttpRequest): the GET request sent to the server
           slug(slug): unique slug field value of the Trip instance

           Returns:
           HttpResponse: the view of the detail template

        """
        trip = self.get_queryset().get(pk=pk)
        context = {
            'trip': trip
        }
        return render(request, self.template_name, context)
