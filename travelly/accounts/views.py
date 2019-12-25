from django.shortcuts import render
from accounts.forms import SignUpForm
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView)
from django.views.generic.detail import DetailView
from accounts.models import Profile
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


def launch_page(request):
    '''Return the landing page template.'''
    return render(request, 'accounts/home.html')


class SignUpView(SuccessMessageMixin, CreateView):
    '''Allows site visitors to set up a new account with Profile.'''
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')  # not implemented yet
    template_name = 'accounts/signup.html'
    success_message = "Congratulations! You may now log in to Travelly."

    def form_valid(self, form):
        '''Save the new User, and set up their profile as well.'''
        self.object = form.save()
        profile = Profile.objects.create(user=self.object)
        profile.save()
        return super().form_valid(form)
