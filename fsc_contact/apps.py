"""
fsc_contact/apps.py: config file for products app

"""

# - - - - - Django Imports - - - - - - - - -
from django.apps import AppConfig


class FscContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fsc_contact'
