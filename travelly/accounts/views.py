from django.shortcuts import render


def launch_page(request):
    '''Return the landing page template.'''
    return render(request, 'accounts/home.html')
