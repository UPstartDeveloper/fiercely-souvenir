from django.shortcuts import render


def show_options(request):
    '''Show options to request ride or hotel reservations.'''
    return render(request, 'airports/index.html')
