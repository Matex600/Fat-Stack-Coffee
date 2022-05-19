"""

fsc_store/apps.py: config file for home app

"""

# - - - - - Django Imports - - - - - - - - -
from django.apps import AppConfig


class FscStoreConfig(AppConfig):
    """
    Store app Config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fsc_store'
