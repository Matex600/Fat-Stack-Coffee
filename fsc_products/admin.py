"""

fsc_products/admin.py: Admin models for superuser  with models
Category and Product. Based on admin in
Code Institute's Boutique Ado project.

"""

# - - - - - Django Imports - - - - - - - - -
from django.contrib import admin

# - - - - - Internal imports - - - - - - - -
from .models import Product, Category


class ProductsAdmin(admin.ModelAdmin):
    """
    The Admin product class
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoriesAdmin(admin.ModelAdmin):
    """
    The Admin category class
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductsAdmin)
admin.site.register(Category, CategoriesAdmin)
