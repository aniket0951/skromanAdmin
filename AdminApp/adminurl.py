from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    #  to open a skroman 
    # path('openskroman/', OpenSkroman),
    path('', OpenSkroman),
    path('loginUser/', LoginUser, name="loginUser"),

]