"""

fsc_users/views.py: views for fsc_users app.
Credit to Code Institute for profile and order_history views.

"""

# - - - - - Django Imports - - - - - - - - -
from django.shortcuts import render, get_object_or_404
from django.contrib import messages


# - - - - - Internal Imports - - - - - - - - -
from .models import UserProfile
from .forms import UserProfileForm


def user_profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'user_profiles/user_profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)