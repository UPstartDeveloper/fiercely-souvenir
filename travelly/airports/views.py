from django.shortcuts import render
from airports.models import AirportAddress
from airports.forms import AirportForm
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
from django.contrib.auth.models import User
from django.contrib import messages


class AirportList(ListView):
    '''A list of the airports entered by users.'''
    model = AirportAddress
    template_name = 'airports/index.html'

    def get(self, request):
        """Renders all the AirportAddress objects currently in the database.

           Parameters:
           request(HttpRequest): request sent to server from client

           Returns:
           HttpResponse: a view that displays AirportAddress objects

        """
        airports = self.get_queryset().all()
        return render(request, self.template_name, {'airports': airports})


class AirportCreate(CreateView):
    '''User is able to add an airport.'''
    model = AirportAddress
    form_class = AirportForm
    template_name = 'airports/create.html'
    queryset = AirportAddress.objects.all()


class AirportDetail(DetailView):
    '''User is able to see hotels and car rentals nearby a specific airport.'''
    pass


class AirportUpdate(UpdateView):
    '''User is able to change details for a specific airport.'''
    pass


class AirportDelete(DeleteView):
    '''User is able to delete an airport.'''
    pass
