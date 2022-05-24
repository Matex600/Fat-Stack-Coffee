"""

fsc_store/views.py: Views for home app, rendering the landing page of the site.

"""

# - - - - - Django Imports - - - - - - - - -
from django.shortcuts import render


def index(request):
    """
    Class to display the landing page of the site, index.html.
    """
    return render(request, 'store/index.html')


def about(request):
    """
    Class to display the about page of the site, about_us.html.
    """
    return render(request, 'about/about_us.html')
