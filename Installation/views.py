from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from rest_framework.generics import *
from rest_framework.mixins import *
from django.contrib import messages
from AdminApp.models import *
from AdminApp.adminserializer import *
from django.views.generic.list import ListView
from SalesApp.models import LeadModel
from .models import *
from .inst_serilizer import *


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
            messages.success(request, "New User Addedd Successfully.")
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
    queryset = ComplaintsModel.objects.all().order_by('-id')
    template_name = 'Complaints.html'
    context_object_name = 'leads'

    def get_context_data(self, **kwargs):
        context = super(ComplaintListView, self).get_context_data(**kwargs)
        context['department'] = 'Installation'

        return context


def test(request):
    comdata = ComplaintsModel.objects.all()
    ser = ComplaintSerializer(comdata, many=True)
    for i in ser.data:
        print(i['complaint_des'], i['lead_id']['name'])
    return HttpResponse(ser.data)
