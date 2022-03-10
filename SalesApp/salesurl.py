from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [

    path('usermodes/<str:tag>/', OpenUserModes, name="usermodes"),

    # add a new lead here
    path('leadsclass', LeadClass.as_view(), name='leads'),

    # get a all leads with data
    path('leaddetails/', LeadListView.as_view(), name='leadhome'),

    # update a specific lead and get data of lead
    path('leadedit/<int:pk>/', LeadUpdate.as_view(), name='lead_edit'),

    # client class 
    path('clientclass/', ClientClass.as_view(), name='client'),

    # edit, delete and update use this for client details 
    path('EditClientClass/<int:pk>/', EditClientClass.as_view(), name='edu_client'),

    # client data show
    path('clientdetails/', ClientListView.as_view(), name='client_details'),

    # lead note operation
    path('leadnote/<int:pk>/', LeadNotes.as_view(), name='lead_notes'),

    # add new lead note
    path('lead_note_class/', LeadNoteClass.as_view(), name='lead_note_class'),


    path('SkromanVideo/', SkromanVideo, name='SkromanVideo'),

    path('DeviceImages/', DeviceImages, name='DeviceImages')

]