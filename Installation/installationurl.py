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

    # get all user list and search filters
    path('UserListView/', UserListView.as_view(), name='user_list'),

    # add complaint
    path('ComplaintClass/', ComplaintClass.as_view(), name='complaint_class'),

    path('ComplaintListView/', ComplaintListView.as_view(), name='complaints'),

    # get specific complaint and update complaint details
    path('UpdateComplaintDetails/<int:pk>/', UpdateComplaintDetails.as_view(), name='update_complaint_details'),

    # complaint assign class
    path('ComplaintAssignClass/', ComplaintAssignClass.as_view(), name='complaint_assign'),

    # show assign complete list
    path('AssignComplaintListView/', AssignComplaintListView.as_view(), name='assign_complete'),

    # update a assigned engineer complaints
    path('UpdateAssignComplaint/<int:pk>/', UpdateAssignComplaint.as_view(), name='update_assignee'),

    # get all old assigned engineers data of complaint
    path('GetAllOldEngineers/<int:complaint_assign_id>/', GetAllOldEngineers, name='get_all_old_engineers'),

    # ----------------- installation user ------------------------
    path('UserAssignComplaints/<int:pk>/', UserAssignComplaints.as_view(), name='user_assign_complaints'),
  

]

