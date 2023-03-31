# All the APIs live here

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


# for swagger documentation
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
        data = Product.objects.all()  # getting all the data
        serializer = ProductSerializers(data, context={'request': request},
                                        many=True)  # using the serializer for the format
        return Response(serializer.data)  # returning the data / response (JSON)

    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)  # converting to serializer
        if serializer.is_valid():  # checking if the serializer is valid in response to our Product Schema
            n = serializer.data
            try:
                temp_prod = Product(productName=n['productName'], productOwnerName=n['productOwnerName'],
                                    Developers=n['Developers'], scrumMasterName=n['scrumMasterName'],
                                    startDate=n['startDate'], methodology=n['methodology'])
                temp_prod.save()  # saving the data
                return Response(status=status.HTTP_201_CREATED)  # returning the status
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # if exception returning bad status

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # if exception returning bad status for invalid serializer

    else:
        return HttpResponse("INVALID REQUEST!")  # for trying to make any other types of request


# for swagger documentation
@swagger_auto_schema(
    method='put',
    operation_summary='Update the Product based on the Product ID (productId). DATE FORMAT (YYYY-MM-DD)',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'productName': openapi.Schema(type=openapi.TYPE_STRING),
            'productOwnerName': openapi.Schema(type=openapi.TYPE_STRING),
            'Developers': openapi.Schema(in_=openapi.IN_QUERY, type=openapi.TYPE_ARRAY,
                                         items=openapi.Schema(type=openapi.TYPE_STRING),
                                         description='Array of Developers'),
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
        pk = request.query_params.get('id')  # getting the id from the URL param
        data = Product.objects.get(productId=pk)  # fetching the data
    except data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # if data doesn't exist

    if request.method == 'PUT':
        serializer = ProductSerializers(data, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  # saving the update data
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # for invalid data / serializer

    elif request.method == 'DELETE':
        data.delete()  # deleting the data
        return Response(status=status.HTTP_204_NO_CONTENT)


# for backend healthy endpoint
def health(request):
    return HttpResponse(status=200)


# for swagger documentation
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
        prodId = request.query_params.get('id')  # getting the id from the URL param

        try:
            temp_prod = Product.objects.filter(productId=prodId)  # fetching the data

        except:
            return HttpResponse("DATA DOESN'T EXIST!")  # if data doesn't exist

        serializer = ProductSerializers(temp_prod, context={'request': request}, many=True)
        return Response(serializer.data)  # returning the data, after passed through serializer

    else:
        return HttpResponse("USE GET ONLY")  # to give feedback, that only GET is usable for this


# for swagger documentation
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
    if request.method == 'GET':
        src_txt = str(request.query_params.get('src'))  # getting the search param from the URL param (src short of search)
        if len(src_txt) > 0:  # check to avoid empty search param
            data = Product.objects.filter(Q(scrumMasterName__icontains=src_txt) | Q(Developers__icontains=src_txt))
            # for the above line we are using Q that helps with complex or encapsulation query, so I nested the query in one
            # to search for either Scrum Master or Developer, the __icontains helps to search for any substring
            # so that if a name is big we don't have to search by writing the whole name which make user experience bad

        serializer = ProductSerializers(data, context={'request': request}, many=True)
        return Response(serializer.data)  # returning the data after passing through serializer

    else:
        return HttpResponse("USE GET ONLY") # to give feedback, that only GET is usable for this
