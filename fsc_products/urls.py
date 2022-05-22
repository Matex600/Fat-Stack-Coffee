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
    path("add_review/<product_id>", views.add_review, name="add_review"),
    path("edit_review/<int:review_id>", views.edit_review, name="edit_review"),
    path("delete_review/<review_id>", views.delete_review,
         name="delete_review"),
]
