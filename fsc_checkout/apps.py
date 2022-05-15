"""

checkout/apps.py: config file for checkout app

"""


# - - - - - Django Imports - - - - - - - - -
from django.apps import AppConfig


class FscCheckoutConfig(AppConfig):
    name = 'fsc_checkout'

    def ready(self):
        # pylint: disable=unused-import, import-outside-toplevel
        import fsc_checkout.signals # noqa