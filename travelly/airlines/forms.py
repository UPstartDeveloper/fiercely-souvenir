from airlines.models import Airline, Review
from django import forms


class AirlineForm(forms.ModelForm):
    '''A form based on the Airline model.'''
    class Meta:
        model = Airline
        fields = ['title', 'logo']
