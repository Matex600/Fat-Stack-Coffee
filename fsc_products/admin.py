from django.contrib import admin
from .models import Product, Category


class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'prod_name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductsAdmin)
admin.site.register(Category, CategoriesAdmin)