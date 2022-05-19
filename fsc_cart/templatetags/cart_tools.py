"""

cart/cart_tools.py: tools for cart app

"""

# - - - - - Django Imports - - - - - - - - -
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculates the subtotal of each item in the
    shopping cart.
    Args:
        price (decimal)
        quantity(integer)
    Returns:
        The result of price mulitplied by quantity
    """
    return price * quantity
