from multiprocessing import context

from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from rest_framework.generics import *
from rest_framework.mixins import *
from django.contrib import messages
# from AdminApp.models import *
from AdminApp.adminserializer import *
from django.views.generic.list import ListView
from SalesApp.models import LeadModel
from .models import *
from .inst_serilizer import *
from django.db.models import Q


from django.contrib import auth
from django.contrib.auth import forms
from django.core import paginator
from django.db import connection
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import EmptyPage, Page, Paginator
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.hashers import make_password, check_password
from passlib.hash import pbkdf2_sha256

from django.contrib import messages

from django.core import serializers
from django.http import JsonResponse
from .models import *
from django.utils.datastructures import MultiValueDictKeyError
import requests



# Create your views here.
def OpenInstallation(request, tag):
    # context = {'department': 'Installation'}
    if tag == 'installation':
        return redirect('lead_list')
    elif tag == 'adduser':
        return redirect('user_list')
    elif tag == 'addNewUser':
        context = {}
        context['department'] = 'Installation'
        context['edit'] = 'addForm'
        return render(request, 'AddNewUser.html', context)
    else:
        return HttpResponse("no matched tag")


def OpenAddComplaint(request, lead_id):
    context = {
        'lead_id': lead_id,
        'department': 'Installation'
    }
    return render(request, "AddComplaints.html", context)


# add new user installation
class InstallationUser(CreateModelMixin, GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        add = self.create(request, *args, **kwargs)
        if add:
            messages.success(request, "New User Added Successfully.")
            return redirect('user_list')


class InstallationPKClass(UpdateModelMixin, RetrieveModelMixin, GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_update = self.update(request, *args, **kwargs)
        if user_update:
            messages.success(self.request, "User details updated successfully")
            return redirect('user_list')

    def get(self, request, *args, **kwargs):
        context = {
            'data': self.get_object(),
            'edit': 'edit',
            'department': 'Installation'
        }
        return render(self.request, 'AddNewUser.html', context)


class UserListView(ListView):
    queryset = Users.objects.all().order_by('-id')
    template_name = 'AddNewUser.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['department'] = 'Installation'
        context['edit'] = 'show'
        return context


# get all leads details
class LeadListView(ListView):
    queryset = LeadModel.objects.all().order_by('-id')
    template_name = 'InstallationHome.html'
    context_object_name = 'leads'

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        context['department'] = 'Installation'
        return context



# add or get complaints
class ComplaintClass(CreateModelMixin, GenericAPIView):
    queryset = ComplaintsModel.objects.all()
    serializer_class = ComplaintSerializer

    def post(self, request, *args, **kwargs):
        complaint = self.create(request, *args, **kwargs)
        if complaint:
            messages.success(self.request, "New Complaint Added Successfully")
            return redirect('lead_list')


class ComplaintListView(ListView):
    queryset = ComplaintsModel.objects.filter(~Q(complaint_status="Assign")).all().order_by('-id')
    template_name = 'Complaints.html'
    context_object_name = 'complaints'

    def get_context_data(self, **kwargs):
        context = super(ComplaintListView, self).get_context_data(**kwargs)
        data = ComplaintSerializer(self.queryset, many=True)
        user = Users.objects.filter(user_dept="Installation").all()
        context['users'] = user
        context['department'] = 'Installation'
        
        return context


# assign the complaint
class ComplaintAssignClass(ListModelMixin,CreateModelMixin, GenericAPIView):
    queryset = ComplaintAssignModel.objects.all()
    serializer_class = ComplaintAssignSerializer

    def post(self, request, *args, **kwargs):
        insert = self.create(request, *args, **kwargs)
        if insert:
            complaint_id = self.request.POST.get('complaint_id')
            complaint_update = ComplaintsModel.objects.filter(id=complaint_id).update(complaint_status="Assign")

        messages.success(request, "Complaint assigned successfully")    
        return redirect('complaints')
     

# show all assign complaints 
class AssignComplaintListView(ListModelMixin, GenericAPIView):
    queryset = ComplaintAssignModel.objects.all()
    serializer_class = ComplaintAssignSerializer
    

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ComplaintAssignSerializer(queryset, many=True)
        for i in serializer.data:
            print(i)
        context = {
            "department" : "Installation",
            "data": serializer.data,
            "assign": "assign-show" 
        }
        return render(self.request, "Complaints.html", context)