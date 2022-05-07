from django.shortcuts import render
from .models import Product


def fsc_products(request):

    products = Product.object.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)