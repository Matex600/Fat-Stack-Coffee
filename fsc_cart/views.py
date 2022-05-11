from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):

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
            else:
                cart[item_id]['items_by_weight'][weight] = quantity
        else:
            cart[item_id] = {'items_by_weight': {weight: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    weight = None
    if 'product_weight' in request.POST:
        weight = request.POST['product_weight']
    cart = request.session.get('cart', {})

    if weight:
        if quantity > 0:
            cart[item_id]['items_by_weight'][weight] = quantity
        else:
            del cart[item_id]['items_by_weight'][weight]
            if not cart[item_id]['items_by_weight']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse(view_cart))


def delete_from_cart(request, item_id):

    try:
        weight = None
        if 'product_weight' in request.POST:
            weight = request.POST['product_weight']
        cart = request.session.get('cart', {})

        if weight:
            del cart[item_id]['items_by_weight'][weight]
            if not cart[item_id]['items_by_weight']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
