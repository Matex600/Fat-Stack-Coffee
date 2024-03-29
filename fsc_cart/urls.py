"""

fsc_cart/urls.py: the urls to connect the cart views with their templates.

"""
# - - - - - Django Imports - - - - - - - - -
from django.urls import path

# - - - - - Internal imports - - - - - - - - -
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<item_id>/', views.update_cart, name='update_cart'),
    path('remove/<item_id>/', views.delete_from_cart, name='delete_from_cart'),
]
