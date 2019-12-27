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
from airlines.forms import AirlineForm


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


class AirlineDetail(DetailView):
    '''A look at an airline with all its reviews underneath.'''
    model = Airline
    template_name = 'airlines/airline/details.html'

    def get(self, request, slug):
        """Renders a page to show the boarding instructions for a single Trip.

           Parameters:
           request(HttpRequest): the GET request sent to the server
           slug(slug): unique slug field value of the Airline instance

           Returns:
           HttpResponse: the view of the detail template

        """
        airline = self.get_queryset().get(slug__iexact=slug)
        reviews = Review.objects.filter(airline=airline)
        context = {
            'airline': airline,
            'reviews': reviews
        }
        return render(request, self.template_name, context)


class AirlineCreate(LoginRequiredMixin, CreateView):
    '''Submit a form to create new Airline.'''
    model = Airline
    form_class = AirlineForm
    template_name = 'airlines/airline/create.html'
    login_url = 'accounts:login'

    def form_valid(self, form):
        '''Initializes author and image (if there is one) of new Note.'''
        form.instance.logo = self.request.FILES.get('logo')
        return super().form_valid(form)
