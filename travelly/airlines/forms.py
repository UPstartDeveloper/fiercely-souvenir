from airlines.models import Airline, Review
from django import forms


class AirlineForm(forms.ModelForm):
    '''A form based on the Airline model.'''
    class Meta:
        model = Airline
        fields = ['title', 'logo']


class ReviewForm(forms.ModelForm):
    '''Form class based on the Review model.'''
    class Meta:
        model = Review
        fields = [
            'airline',
            'headline',
            'rating',
            'comments',
            'price'
        ]
