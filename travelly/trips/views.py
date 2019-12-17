from django.shortcuts import render

# Create your views here.


def hello_world(request):
    '''Display hello world. Base for building front-end first site.'''
    return render(request, 'trips/index.html')
