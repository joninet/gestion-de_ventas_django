from ast import Try
from sys import api_version

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def productList(request):
    if request.method == 'GET':
        #obtenemos todos los productos
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    #creamos un nuevo producto
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=200)

@api_view(['GET', 'PUT', 'DELETE'])
def productDetail(request, pk):
    try:
        product = Product.objects.get(pk=pk)

    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=200)

    elif request.method == 'DELETE':
        #delete product
        product.delete()
        return Response(status=204)

