from django.contrib import admin
from django.urls import path, include
from Production.views import *
from SalesApp.models import LeadModel
from .models import *

urlpatterns = [
    

    path('Production_Request/',Production_Request, name='Production_Request' ),

    # path('Production_Request/',Production_Request.as_view(), name='InventoryHome' ),

    path('ProductionHome/',LeadListView.as_view(), name='ProductionHome' ),

    # ProductionUser
    path('production_user/<int:pk>/',ProductionUser.as_view(), name='production_user' ),
]
