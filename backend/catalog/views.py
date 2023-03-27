from django.shortcuts import render
from .models import Product
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse


@api_view(['GET', 'POST'])
def products_api(request):
    """
    Test will add doc later

    {
    "productName": "My Product 2",
    "productOwnerName": "John Doe",
    "Developers": [
        "Jane Smith",
        "Bob Johnson"
    ],
    "scrumMasterName": "Alice Lee",
    "startDate": "2023-03-26",
    "methodology": "Agile"
}
    """

    if request.method == 'GET':
        data = Product.objects.all()
        serializer = ProductSerializers(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            n = serializer.data
            try:
                temp_prod = Product(productName=n['productName'], productOwnerName=n['productOwnerName'],
                                    Developers=n['Developers'], scrumMasterName=n['scrumMasterName'],
                                    startDate=n['startDate'], methodology=n['methodology'])
                temp_prod.save()
                return Response(status=status.HTTP_201_CREATED)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("INVALID REQUEST!")


@api_view(['PUT', 'DELETE'])
def data_del_up(request):
    try:
        pk = request.query_params.get('pk')
        data = Product.objects.get(productId=pk)
    except data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProductSerializers(data, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)