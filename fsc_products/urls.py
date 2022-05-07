from django.urls import path
from. import views

urlpatterns = [
    path('', views.fsc_products, name='products')
]