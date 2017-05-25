# -*- coding: utf-8 -*-

# Imports
from django.contrib import admin
from .models import Store
from .models import Product
from .models import Inventory

admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Inventory)
