# -*- coding: utf-8 -*-

# serializers.py

from rest_framework import serializers
from StoreManager.models import Product
from StoreManager.models import Store
from StoreManager.models import Inventory


# -------------------------------------------------------------------
# Product Serializer
# -------------------------------------------------------------------
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Product
        fields = ('product_id', 'title')


# -------------------------------------------------------------------
# Store Inventory Serializer
# -------------------------------------------------------------------
class InventorySerializer(serializers.ModelSerializer):

#    product = serializers.HyperlinkedRelatedField(
#                queryset=Product.objects.all(),
#                view_name='product-detail',
#                many=True)

    product = ProductSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = ('product','onhand')

# -------------------------------------------------------------------
# Store Serializer
# -------------------------------------------------------------------
class StoreSerializer(serializers.ModelSerializer):
#    inventory = serializers.HyperlinkedRelatedField(
#                queryset=Inventory.objects.all(),
#                view_name='storeinventories-detail',
#                many=True)

#    inventory = serializers.SlugRelatedField(
#                    many=True,
#                    read_only=True,
#                    slug_field='product_id')

    inventory = InventorySerializer(many=True,read_only=True)

    class Meta:
        """
        Meta class to map serializer's fields with the model fields.
        """
        model = Store
        fields = ('store_id','name','inventory')


