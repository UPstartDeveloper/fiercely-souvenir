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


def show_trips(request):
    '''Render index for past trips.'''
    return render(request, 'trips/index.html')
