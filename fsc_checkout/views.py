from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KeKyKDmfz3u6CTee543ChF8jQ91zSwWBUh8OhRsK3bqJ4KB4GK9kga6Qk7oEGphW5zf7jV8wBgMojuOiMsXj1vi00sTeu9C0N',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)