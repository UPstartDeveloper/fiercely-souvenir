from trips.models import Trip
from django import forms


class TripForm(forms.ModelForm):
    '''A form based on the Trip model.'''
    class Meta:
        model = Trip
        fields = [
            'title',
            'arrive_at',
            'depart_from',
            'airline'
        ]
