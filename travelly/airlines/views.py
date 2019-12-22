from django.shortcuts import render

# Create your views here.


def show_airlines(request):
    '''Rendrer index for airlines.'''
    return render(request, 'trips/index.html')
