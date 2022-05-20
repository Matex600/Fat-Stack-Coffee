"""

fsc_reviews/urls.py: Contains the admin model for user reviews.

"""

# - - - - - Django Imports - - - - - - - - -
from django.urls import path

# - - - - - Internal Imports - - - - - - - - -
from . import views


urlpatterns = [
    path("add_review/<product_id>", views.add_review, name="add_review"),
    path("edit_review/<int:review_id>", views.edit_review, name="edit_review"),
    path("delete_review/<review_id>", views.delete_review,
         name="delete_review"),
]