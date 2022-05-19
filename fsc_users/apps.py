"""

fsc_users/apps.py: config file for users app

"""

# - - - - - Django Imports - - - - - - - - -
from django.apps import AppConfig


class FscUsersConfig(AppConfig):
    """
    Users app Config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fsc_users'
