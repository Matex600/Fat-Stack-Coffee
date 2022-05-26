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


# - - - - - Error Handling - - - - - - - - -
# As per Documentation recommendation


def handler400(request, exception):
    """
    Handler for Bad Request 400.
    """
    return render(request, "400.html", status=400)


def handler403(request, exception):
    """
    Handler forbidden request 403.
    """
    return render(request, "403.html", status=403)


def handler404(request, exception):
    """
    Handler for not found request 404.
    """
    return render(request, "404.html", status=404)


def handler500(request, *args, **argv):
    """
    Handler for internal server error generic message 500.
    """
    return render(request, "500.html", status=500)