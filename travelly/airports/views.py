from django.shortcuts import render
from airports.models import AirportAddress
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
    pass


class AirportCreate(CreateView):
    '''User is able to add an airport.'''
    pass


class AirportDetail(DetailView):
    '''User is able to see hotels and car rentals nearby a specific airport.'''
    pass


class AirportUpdate(UpdateView):
    '''User is able to change details for a specific airport.'''
    pass


class AirportDelete(DeleteView):
    '''User is able to delete an airport.'''
    pass
