from django.contrib import admin
from django.urls import path, include
from Production.views import *
urlpatterns = [
    

    path('Production_Request/',Production_Request, name='Production_Request' ),

    # path('Production_Request/',Production_Request.as_view(), name='InventoryHome' ),

]
