from django.shortcuts import render

# Create your views here.


def show_trips(request):
    '''Render index for past trips.'''
    return render(request, 'trips/all-trips.html')


def show_airlines(request):
    '''Rendrer index for airlines.'''
    return render(request, 'trips/all-airlines.html')
