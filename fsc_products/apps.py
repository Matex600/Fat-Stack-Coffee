"""
fsc_products/apps.py: config file for products app

"""

# - - - - - Django Imports - - - - - - - - -
from django.apps import AppConfig


class FscProductsConfig(AppConfig):
    """
    Products app Config model
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fsc_products'
