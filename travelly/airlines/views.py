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
from airlines.forms import AirlineForm, ReviewForm
from django.contrib import messages


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
        '''Initializes author and image (if there is one) of new Airline.'''
        form.instance.logo = self.request.FILES.get('logo')
        form.instance.verified = False  # can be changed later by staff
        return super().form_valid(form)


class AirlineUpdate(UpdateView):
    '''Submit a form to edit a pre-existing Airline.'''
    model = Airline
    form_class = AirlineForm
    template_name = 'airlines/airline/edit.html'

    def form_valid(self, form):
        '''Changes the image (if there is a new upload) of the Airline.'''
        upload = self.request.FILES.get('logo')
        if upload is not None:
            form.instance.logo = upload
        return super().form_valid(form)


class ReviewCreate(LoginRequiredMixin, CreateView):
    '''Submit a form to create a new review of an airline.'''
    model = Review
    form_class = ReviewForm
    template_name = 'airlines/review/create.html'
    login_url = 'accounts:login'

    def form_valid(self, form):
        '''Initialize the author of the new Review instance.'''
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewUpdate(UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'airlines/review/edit.html'

    def test_func(self):
        '''Ensures that Reviews can only be edited by who posted them.'''
        review = self.get_object()
        return (self.request.user == review.author)


class ReviewDelete(UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'airlines/review/delete.html'
    success_url = reverse_lazy('airlines:all-airlines')
    success_message = "Your review has been deleted."
    queryset = Review.objects.all()

    def delete(self, request, *args, **kwargs):
        '''Delete the Review instance, and message the user about it.'''
        messages.success(request, self.success_message)
        return super().delete(request)

    def test_func(self):
        '''Ensure Reviews can only be deleted by the user who posted them.'''
        review = self.get_object()
        return (self.request.user == review.author)
