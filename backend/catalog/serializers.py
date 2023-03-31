from rest_framework import serializers
from catalog.models import Product

# serializer for the Product model for all the fields


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
