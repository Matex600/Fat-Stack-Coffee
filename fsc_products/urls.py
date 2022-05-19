"""

fsc_products/urls.py: All urls for the products app.

"""

from django.urls import path
from. import views

urlpatterns = [
    path('', views.fsc_products, name='products'),
    path('<int:product_id>/', views.fsc_product_detail, name='product_detail'),
    path('add/', views.fsc_add_product, name='fsc_add_product'),
    path(
        'edit/<int:product_id>/',
        views.fsc_edit_product, name='fsc_edit_product'),
    path(
        'delete/<int:product_id>/',
        views.fsc_delete_product, name='fsc_delete_product'),
]
