from django.urls import path
from. import views

urlpatterns = [
    path('', views.fsc_products, name='products'),
    path('<int:product_id>/', views.fsc_product_detail, name='product_detail'),
    path('add/', views.fsc_add_product, name='fsc_add_product'),
]