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
from notes.forms import NoteForm


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
