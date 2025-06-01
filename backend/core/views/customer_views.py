from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Customer
from ..serializers import CustomerSerializer


@api_view(['GET', 'POST'])
def customerList(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=200)

@api_view(['GET', 'PUT', 'DELETE'])
def customerDetail(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)

    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=404)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=200)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=204)

    
        