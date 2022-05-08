from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def fsc_products(request):

    products = Product.objects.all()

    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please try to specify \
                                         your search query!")
                return redirect(reverse('products'))
            
            queries = (
                Q(prod_name__icontains=query) | Q(description__icontains=query))
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }
    return render(request, 'products/products.html', context)


def fsc_product_detail(request, product_id):

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'product': products,
    }
    return render(request, 'products/products.html', context)