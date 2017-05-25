# -*- coding: utf-8 -*-

#####################################################################
#
# File: views.py
# Auth: Gerik Peterson
#
#
#####################################################################

from rest_framework import viewsets

from StoreManager.models import Product
from StoreManager.models import Store
from StoreManager.models import Inventory
from StoreManager.serializers import ProductSerializer
from StoreManager.serializers import InventorySerializer
from StoreManager.serializers import StoreSerializer

# -------------------------------------------------------------------
# Stores
# -------------------------------------------------------------------
class StoreViewSet(viewsets.ModelViewSet):
    """
    Store `list`, `create`, `retrieve`, `update`, and `destroy` actions
    """
#    data = Store.objects.select_related('inventory').all()
#    print("StoreViewSet: data=",data)
#    queryset = Store.objects.all().prefetch_related('inventory')
    queryset = Store.objects.order_by('name')
    serializer_class = StoreSerializer

#    def get_queryset(self):
#        stores = Store.objects.all().prefetch_related('inventory')
#        print("views.StoreViewSet.get_queryset: stores = ",stores)
#        return stores

#    def perform_retrieve(self, serializer):
#        queryset = Store.objects.filter(pk=1)




# -------------------------------------------------------------------
# Products
# -------------------------------------------------------------------
class ProductViewSet(viewsets.ModelViewSet):
    """
    Store `list`, `create`, `retrieve`, `update`, and `destroy` actions
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# -------------------------------------------------------------------
# Invetory View
# -------------------------------------------------------------------
class InventoryViewSet(viewsets.ModelViewSet):
    """
    Invetory `list`, `create`, `retrieve`, `update`, and `destroy` actions
    """
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer






