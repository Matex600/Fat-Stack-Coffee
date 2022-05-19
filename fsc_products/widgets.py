"""

fsc_product/widgets.py: Allows customisation of the image field for a product.
This functionality is derived from the Boutique Ado project with
Code Institute.

"""

# - - - - - Django Imports - - - - - - - - - - - - -
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'products/custom_widget_templates/custom_clearable_file_input.html'
    )
