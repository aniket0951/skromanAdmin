from django.contrib import admin
from django.urls import path, include
from Inventory.views import *
urlpatterns = [
    

    path('Add_BOM',Add_BOM.as_view(), name='Add_BOM' ),

    path('BOM_list',BOM_list.as_view(), name='BOM_list' ),


    path('InventoryHome/',OpenUser.as_view(), name='InventoryHome' ),

]
