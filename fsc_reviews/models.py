"""

fsc_reviews/models.py: Contains the model for user reviews.

"""

# - - - - - Django Imports - - - - - - - - -
from django.db import models

# - - - - - Internal Imports - - - - - - - - -
from fsc_products.models import Product
from fsc_users.models import UserProfile


class Review(models.Model):
    """
    The review model class, with fields for
    user and products using a foreign key (unique value)
    A prod_description and review_date
    """

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    prod_desc = models.TextField(max_length=450, null=False,
                                 blank=False)
    review_time = models.DateTimeField(auto_now_add=True)
