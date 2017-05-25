# -*- coding: utf-8 -*-

# Imports
from django.db import models
from django.utils import timezone

import datetime

# -------------------------------------------------------------------
# Store Model
# -------------------------------------------------------------------
class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)

    # A Store HAS (pk<<<fk) inventoryitems

    def __str__(self):
        return self.name

# -------------------------------------------------------------------
# Product Model
# -------------------------------------------------------------------
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title



# -------------------------------------------------------------------
# Inventory Mapping Model for Stores and their Products
# -------------------------------------------------------------------
class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.PROTECT, related_name='inventory')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='products')
    onhand = models.IntegerField()

    class Meta:
        unique_together = (('store','product'),)


    def __str__(self):
        return str(self.store) + ":" + str(self.product)



