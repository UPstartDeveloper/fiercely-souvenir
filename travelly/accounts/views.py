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
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views


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


class ProfileDetail(UserPassesTestMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile/view.html'
    login_url = 'accounts:login'
    queryset = User.objects.all()

    def get(self, request, pk):
        """Renders a page to show a specific note in full detail.
           Parameters:
           user_id(int): pk of the User object requesting the page
           request(HttpRequest): the HTTP request sent to the server

           Returns:
           render: a page of the Profile information

        """
        user = self.queryset.get(id=pk)
        profile = user.profile
        context = {
            'profile': profile
        }
        return render(request, self.template_name, context)

    def test_func(self):
        '''Ensures that users can only view their own Profiles.'''
        user = self.get_object()
        return (self.request.user.profile == user.profile)


class AccountUpdate(UserPassesTestMixin, UpdateView):
    '''User is allowed to change their own account information.'''
    model = User
    template_name = 'accounts/profile/change-info.html'
    fields = ['username', 'email', 'first_name', 'last_name']
    queryset = User.objects.all()

    def get_success_url(self):
        '''Redirect to the profile page of the User.'''
        url = self.object.profile.get_absolute_url()
        return url

    def test_func(self):
        '''Ensure only the User can change their own account information.'''
        user = self.get_object()
        return (self.request.user == user)


class UserDelete(UserPassesTestMixin, DeleteView):
    '''User is able to delete their own account from the database.'''
    model = User
    template_name = 'accounts/profile/delete.html'
    success_url = reverse_lazy('accounts:login')
    # queryset = User.objects.all()

    def get(self, request, pk):
        """Renders a page with a form to delete the User account.

           Parameters:
           request(HttpRequest): request sent to the server from the client
           pk(int): the value of the id field of the specific User instance

           Returns:
           HttpResponse: the TemplateResponse with the delete form

        """
        user = self.get_queryset().get(id=pk)
        return render(request, self.template_name)

    def test_func(self):
        '''Ensure that only users can delete their own accounts on the site.'''
        user = self.get_object()
        return (self.request.user.profile == user.profile)


class BeginPasswordChange(SuccessMessageMixin,
                          auth_views.PasswordChangeView):
    '''User is able to change their password.'''
    template_name = 'accounts/password/password-change.html'
    success_url = reverse_lazy('accounts:acct_info')
    success_message = 'Your password was changed successfully!'
    queryset = User.objects.all()

    def get(self, request, pk):
        """Renders a page with a form to delete the User account.

           Parameters:
           request(HttpRequest): request sent to the server from the client
           pk(int): the value of the id field of the specific User instance

           Returns:
           HttpResponse: the TemplateResponse with the delete form

        """
        user = self.queryset.get(id=pk)
        return render(request, self.template_name)
