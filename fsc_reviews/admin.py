"""

fsc_reviews/admin.py: Contains the admin model for user reviews.

"""

# - - - - - Django Imports - - - - - - - - -
from django.contrib import admin

# - - - - - Internal Imports - - - - - - - - -
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin class for Review model
    With list_display to show fields
    to user
    """
    list_display = (
        'product',
        'user',
        'review_time'
    )
