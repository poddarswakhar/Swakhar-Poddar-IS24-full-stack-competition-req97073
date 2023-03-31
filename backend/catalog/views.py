from django.shortcuts import render
from drf_yasg import openapi

from .models import Product
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='GET',
    operation_summary='Get all the Product Data',
    responses={200: 'OK'}
)
@swagger_auto_schema(
    method='POST',
    operation_summary='Create Product Data',
    request_body=ProductSerializers,
    responses={201: 'Created'}
)
@api_view(['GET', 'POST'])
def products_api(request):
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


@swagger_auto_schema(
    method='put',
    operation_summary='Update the Product based on the Product ID (productId). DATE FORMAT (YYYY-MM-DD)',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'productName': openapi.Schema(type=openapi.TYPE_STRING),
            'productOwnerName': openapi.Schema(type=openapi.TYPE_STRING),
            'Developers': openapi.Schema(in_=openapi.IN_QUERY, type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING), description='Array of Developers'),
            'scrumMasterName': openapi.Schema(type=openapi.TYPE_STRING),
            'startDate': openapi.Schema(type=openapi.FORMAT_DATE),
            'methodology': openapi.Schema(type=openapi.TYPE_STRING)
        },
        required=['productName', 'productOwnerName', 'Developers', 'scrumMasterName', 'startDate', 'methodology']
    ),
    responses={200: 'OK', 400: 'Bad Request', 404: 'Not Found'},
    manual_parameters=[
        openapi.Parameter(
            name='id',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_INTEGER,
            description='productId'
        )
    ]
)
@swagger_auto_schema(
    method='DELETE',
    operation_summary='Delete the Product Data based on the Product ID (productId)',
    responses={200: 'OK'},
    manual_parameters=[
        openapi.Parameter(
            name='id',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_INTEGER,
            description='productId'
        )
    ]
)
@api_view(['PUT', 'DELETE'])
def data_del_up(request):
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


@swagger_auto_schema(
    method='GET',
    operation_summary='Get all the Product Data based on the Product ID (productId)',
    responses={200: 'OK'},
    manual_parameters=[
        openapi.Parameter(
            name='id',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_INTEGER,
            description='productId'
        )
    ]
)
@api_view(['GET'])
def products_api_ret(request):
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


@swagger_auto_schema(
    method='GET',
    operation_summary='Get all the Product Data based on the Search Parameter for Scrum Master or Developer Name',
    responses={200: 'OK'},
    manual_parameters=[
        openapi.Parameter(
            name='src',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description='Name For (Scrum Master or Developer)'
        )
    ]
)
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
