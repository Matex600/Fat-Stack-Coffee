"""

fsc_contact/forms.py: forms to be used with the product app of the application

"""

# - - - - - Django Imports - - - - - - - - -
from django.forms import ModelForm

# - - - - - Internal imports - - - - - - - - -
from .models import Contact


class ContactForm(ModelForm):
    """
    Form for Contact model that uses all fields
    """
    class Meta:
        model = Contact
        fields = '__all__'
