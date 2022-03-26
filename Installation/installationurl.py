from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('OpenInstallation/<str:tag>/', OpenInstallation, name='installation'),

    path('OpenAddComplaint/<int:lead_id>/', OpenAddComplaint, name='open_complaint'),

    # show all lead information to installation user
    path('LeadListView/', LeadListView.as_view(), name='lead_list'),

    # add new user
    path('InstallationUser/', InstallationUser.as_view(), name='installation_user'),

    # to pk based operation
    path('InstallationPKClass/<int:pk>/', InstallationPKClass.as_view(), name='installation_pk'),

    # get all user list
    path('UserListView/', UserListView.as_view(), name='user_list'),

    # add complaint
    path('ComplaintClass/', ComplaintClass.as_view(), name='complaint_class'),

    path('ComplaintListView/', ComplaintListView.as_view(), name='complaints'),

    path('test/', test),



]

