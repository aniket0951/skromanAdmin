from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('OpenInstallation/<str:tag>/', OpenInstallation, name='installation'),

    # add new user
    path('InstallationUser/', InstallationUser.as_view(), name='installation_user'),

    # get all user list
    path('UserListView/', UserListView.as_view(), name='user_list'),
]