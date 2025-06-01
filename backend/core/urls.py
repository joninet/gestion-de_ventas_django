from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.productList, name='product-list'),
    path('products/<int:pk>/', views.productDetail, name='product-detail'),
]