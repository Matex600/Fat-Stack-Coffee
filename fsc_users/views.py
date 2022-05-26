"""

fsc_users/views.py: views for fsc_users app.
Credit to Code Institute for profile and order_history views.

"""

# - - - - - Django Imports - - - - - - - - -
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    )
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# - - - - - Internal Imports - - - - - - - - -
from fsc_products.models import Product, FavouritesList
from fsc_checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm

# pylint: disable=no-member


@login_required
def user_profile(request):
    """
    Display the user's profile and allows user to update
    information, view order history
    as well as letting a user add to favourites
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    try:
        favourites = FavouritesList.objects.filter(user=request.user.id)[0]
    except IndexError:
        favourite_coffee = None
    else:
        favourite_coffee = favourites.product.all()

    if not favourite_coffee:
        messages.info(request, 'You have not added a coffee to favourites :(')

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                'Update failed. Please ensure your details are correct.'
            )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'user_profiles/user_profile.html'
    context = {
        'form': form,
        'orders': orders,
        'favourite_coffee': favourite_coffee,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def add_to_favourites(request, product_id):
    """
    Function based view to show products
    added to favourites by user
    """
    product = get_object_or_404(Product, pk=product_id)
    try:
        favouritesList = get_object_or_404(FavouritesList,
                                           user=request.user.id)

    except Http404:
        favouritesList = FavouritesList.objects.create(user=request.user)
    if product in favouritesList.product.all():
        messages.info(request, 'Your favourites list'
                               'contains this product already,')
    else:
        favouritesList.product.add(product)
        messages.info(
            request, f'Added {product.name[:30]}.. to your Favourites.'
        )
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def delete_from_favourites(request, product_id):
    """
    Function based view to remove
    favourited product for the user
    """
    product = get_object_or_404(Product, pk=product_id)
    favouritesList = get_object_or_404(FavouritesList, user=request.user.id)
    if product in favouritesList.product.all():
        favouritesList.product.remove(product)
        messages.info(
            request, f'Removed {product.name[:30]} from your favourites'
        )
    else:
        messages.error(
            request, (
                f'{product.name[:30]}.. can not be found in your favourites.'
            )
        )

    return redirect(request.META.get('HTTP_REFERER'))


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
