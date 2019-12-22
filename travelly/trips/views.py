from django.shortcuts import render

# Create your views here.


def show_trips(request):
    '''Render index for past trips.'''
    return render(request, 'trips/index.html')
