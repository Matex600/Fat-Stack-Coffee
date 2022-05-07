from django.shortcuts import render, get_object_or_404
from .models import Product


def fsc_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def fsc_product_detail(request, product_id):

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'product': products,
    }
    return render(request, 'products/products.html', context)