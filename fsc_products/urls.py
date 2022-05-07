from django.urls import path
from. import views

urlpatterns = [
    path('', views.fsc_products, name='products'),
    path('<product_id>', views.fsc_product_detail, name='products_detail'),
]