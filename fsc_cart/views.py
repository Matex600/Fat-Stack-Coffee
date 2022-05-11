from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from fsc_products.models import Product

def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    weight = None
    if 'product_weight' in request.POST:
        weight = request.POST['product_weight']
    cart = request.session.get('cart', {})

    if weight:
        if item_id in list(cart.keys()):
            if weight in cart[item_id]['items_by_weight'].keys():
                cart[item_id]['items_by_weight'][weight] += quantity
                messages.success(request, f'Updated weight {weight.upper()} {product.name} quantity to {cart[item_id]["items_by_weight"][weight]}')
            else:
                cart[item_id]['items_by_weight'][weight] = quantity
                messages.success(request, f'Added weight {weight.upper()} {product.name} to your shopping cart')
        else:
            cart[item_id] = {'items_by_weight': {weight: quantity}}
            messages.success(request, f'Added weight {weight.upper()} {product.name} to your shopping cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your shopping cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    weight = None
    if 'product_weight' in request.POST:
        weight = request.POST['product_weight']
    cart = request.session.get('cart', {})

    if weight:
        if quantity > 0:
            cart[item_id]['items_by_weight'][weight] = quantity
            messages.success(request, f'Updated weight {weight.upper()} {product.name} quantity to {cart[item_id]["items_by_weight"][weight]}')
        else:
            del cart[item_id]['items_by_weight'][weight]
            if not cart[item_id]['items_by_weight']:
                cart.pop(item_id)
            messages.success(request, f'Removed item{weight.upper()} {product.name} from your shopping cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your shopping cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_from_cart(request, item_id):

    product = get_object_or_404(Product, pk=item_id)

    try:
        weight = None
        if 'product_weight' in request.POST:
            weight = request.POST['product_weight']
        cart = request.session.get('cart', {})

        if weight:
            del cart[item_id]['items_by_weight'][weight]
            if not cart[item_id]['items_by_weight']:
                cart.pop(item_id)
            messages.success(request, f'Removed weight {weight.upper()} {product.name} from your shopping cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your shopping cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
