"""

fsc_store/views.py: Views for home app, rendering the landing page of the site.

"""

# - - - - - Django Imports - - - - - - - - -
from django.shortcuts import render


def index(request):
    """
    View to display the landing page of the site, index.html.
    """
    return render(request, 'store/index.html')


def about(request):
    """
    View to display the about page of the site, about_us.html.
    """
    return render(request, 'about/about_us.html')


def terms(request):
    """
    View to display Terms and Conditions
    """
    return render(request, 'store/terms.html')


def privacy(request):
    """
    View to display Privacy Policy
    """
    return render(request, 'store/privacy.html')