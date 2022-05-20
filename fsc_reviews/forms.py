"""

fsc_reviews/forms.py: Contains the form class for user reviews.

"""

# - - - - - Django Imports - - - - - - - - -
from django import forms

# - - - - - Internal Imports - - - - - - - - -
from .models import Review


class ReviewForm(forms.ModelForm):
    """ Form for users to add reviews of products"""
    class Meta:
        model = Review
        fields = ('description',)