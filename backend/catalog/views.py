from django.shortcuts import render
from .models import Product
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.db.models import Q


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
    """
    will add later
    http://127.0.0.1:3000/api/catalog/ret/?id=1
    """
    try:
        pk = request.query_params.get('id')
        data = Product.objects.get(productId=pk)
    except data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProductSerializers(data, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def health(request):
    return HttpResponse(status=200)


@api_view(['GET', 'POST'])
def products_api_ret(request):
    """
    test will add later
    http://127.0.0.1:3000/api/catalog/ret/?id=1
    """

    if request.method == 'GET':
        prodId = request.query_params.get('id')

        try:
            temp_prod = Product.objects.filter(productId=prodId)

        except:
            return HttpResponse("DATA DOESN'T EXIST!")

        serializer = ProductSerializers(temp_prod, context={'request': request}, many=True)
        return Response(serializer.data)

    else:
        return HttpResponse("USE GET ONLY")


@api_view(['GET'])
def search(request):
    """
    http://localhost:3000/api/catalog/src/?src=Alice%20Leex
    """
    if request.method == 'GET':
        src_txt = str(request.query_params.get('src'))
        if len(src_txt) > 0:
            data = Product.objects.filter(Q(scrumMasterName__icontains=src_txt) | Q(Developers__icontains=src_txt))

        serializer = ProductSerializers(data, context={'request': request}, many=True)
        return Response(serializer.data)

    else:
        return HttpResponse("USE GET ONLY")
