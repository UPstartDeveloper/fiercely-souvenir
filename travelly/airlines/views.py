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
from airlines.models import Airline, Review
from django.contrib.auth.models import User


class AirlineList(ListView):
    '''An index of all the airlines in the database currently.'''
    model = Airline
    template_name = 'airlines/airline/index.html'

    def get(self, request):
        """Renders all the AIrline objects currently in the database.

           Parameters:
           request(HttpRequest): request sent to server from client

           Returns:
           HttpResponse: a view that displays Airline instances

        """
        airlines = self.get_queryset().all()
        return render(request, self.template_name, {'airlines': airlines})
