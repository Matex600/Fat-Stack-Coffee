"""
fsc_products/forms.py: forms to be used with the product app of the application
Credit to Code Institute for product and order_history views.
"""

# - - - - - Django Imports - - - - - - - - -
from django import forms


# - - - - - Internal Imports - - - - - - - - -
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'