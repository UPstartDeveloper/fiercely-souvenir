from django import forms
from airports.models import AirportAddress


class AirportForm(forms.ModelForm):
    '''A form based on the AirportAddress model fields.'''
    class Meta:
        model = AirportAddress
        fields = [
            'title', 'location'
        ]
