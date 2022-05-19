"""

fsc_products/models.py: Contains the models Category and Product.
Inspired by Code Institute's Boutique Ado project.

"""

# - - - - - Django Imports - - - - - - - - -
from django.db import models


class Category(models.Model):
    """
    The Category model class, with fields for the category name.
    """
    class Meta:
        """
        Meta class to return plural name of category.
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def __str__(self):
        """
        Returns the category name as string.
        Args:
            self (object)
        Returns:
            The category name field as string
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the user readable category name as string.
        Args:
            self (object)
        Returns:
            The category friendly name string
        """
        return self.friendly_name


class Product(models.Model):
    """
    The Product model class, used to generate an instance of a product
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=254
    )
    description = models.TextField()
    coffee_amounts = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    image_url = models.URLField(
        max_length=2024,
        null=True,
        blank=True
    )
    image = models.ImageField(
        max_length=2024,
        null=True,
        blank=True
    )

    def __str__(self):
        """
        Returns the product name
        Args:
            self (object)
        Returns:
            The product name field as string
        """
        return self.name
