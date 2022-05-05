from django.contrib import admin
from django.urls import path, include
from Inventory.views import *
urlpatterns = [
    

    path('Add_BOM/',Add_BOM, name='Add_BOM' ),

    path('InventoryHome/',InventoryHome.as_view(), name='InventoryHome' ),

]
