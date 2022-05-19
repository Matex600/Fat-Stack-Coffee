"""

fsc_store/urls.py: all urls for the home app.

"""

from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='store')
]
