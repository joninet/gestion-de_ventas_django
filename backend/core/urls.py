from django.urls import path

from .views.customer_views import customerDetail, customerList
from .views.product_views import productDetail, productList

urlpatterns = [
    #products
    path('products/', productList, name='product-list'),
    path('products/<int:pk>/', productDetail, name='product-detail'),
    
    #customers
    path('customers/', customerList, name='customer-list'),
    path('customers/<int:pk>/', customerDetail, name='customer-detail'),


]