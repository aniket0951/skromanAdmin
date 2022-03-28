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
from django.db.models import Q
import datetime


# Create your views here.
# open a different pages of installation
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


# to update a installation user information
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


# get all installation users
class UserListView(ListView):
    queryset = Users.objects.all().order_by('-id')
    template_name = 'AddNewUser.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['department'] = 'Installation'
        context['edit'] = 'show'
        search = self.request.GET.get('search')
        if search:
            data = self.get_queryset().filter(
                Q(name__icontains=search) | Q(user_dept__icontains=search) | Q(designation__icontains=search)).all()
            serializers = UserSerializer(data, many=True)
            context.update({"users": serializers.data})

        return context


# get all leads details
class LeadListView(ListView):
    queryset = LeadModel.objects.all().order_by('-id')
    template_name = 'InstallationHome.html'
    context_object_name = 'leads'

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        context['department'] = 'Installation'
        search = self.request.GET.get('search')
        if search:
            data = self.get_queryset().filter(Q(name__icontains=search) | Q(contact__icontains=search)
                                              | Q(site_name__icontains=search) | Q(city__icontains=search)
                                              | Q(pin_code__icontains=search) | Q(ctime__icontains=search))\
                                         .all()
            serializers = LeadSerializer(data, many=True)
            context.update({"leads": serializers.data})

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


#  get all complaints
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


# get and update a complaint details
class UpdateComplaintDetails(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = ComplaintsModel.objects.all()
    serializer_class = ComplaintSerializer

    def get(self, request, *args, **kwargs):
        date = (self.get_object().appointment_date)

        context = {
            'department': 'Installation',
            "assign": "complaint_update",
            "data": self.get_object(),
            "appointment_date": date.strftime(str(date))
        }
        return render(request, "AddComplaints.html", context)

    def post(self, request, *args, **kwargs):
        update = self.update(request, *args, **kwargs)
        if update:
            messages.success(request, "Complaint details updated successfully")
            return redirect('complaints')

        # assign the complaint


class ComplaintAssignClass(RetrieveModelMixin, CreateModelMixin, GenericAPIView):
    queryset = ComplaintAssignModel.objects.all()
    serializer_class = ComplaintAssignSerializer

    def post(self, request, *args, **kwargs):
        insert = self.create(request, *args, **kwargs)
        if insert:
            complaint_id = self.request.POST.get('complaint_id')
            complaint_update = ComplaintsModel.objects.filter(id=complaint_id).update(complaint_status="Assign")

        messages.success(request, "Complaint assigned successfully")
        return redirect('complaints')


# display all complaints with assigned details
class AssignComplaintListView(ListView):
    queryset = ComplaintAssignModel.objects.all()
    template_name = 'Complaints.html'
    context_object_name = 'assign_complete'

    def get_context_data(self, **kwargs):
        context = super(AssignComplaintListView, self).get_context_data(**kwargs)
        # data = ComplaintSerializer(self.queryset, many=True)
        user = Users.objects.filter(user_dept="Installation").all()
        context['users'] = user
        context['department'] = 'Installation'
        context["assign"] = "assign-show"

        # search by placeholder
        search = self.request.GET.get('search')
        if search:
            data = self.get_queryset().filter(Q(complaint_id__lead_id__name__icontains=search) | Q(complaint_id__lead_id__site_name__icontains=search)
                                             | Q (complaint_id__lead_id__contact__icontains=search) | Q(complaint_id__lead_id__city__icontains=search)
                                             | Q (complaint_id__appointment_date__icontains=search))\
                                              .all()
            
            context.update({"assign_complete": data})

        # date filter searching
        startdate = self.request.GET.get('startdate')
        enddate = self.request.GET.get('enddate')
        if startdate and enddate:
            data = self.get_queryset().filter(ctime____range=[str(startdate), str(enddate)], lookup_expr='date__gte').all()
            context.update({"assign_complete": data})

        return context


# update a complete assign engineer installation
class UpdateAssignComplaint(UpdateModelMixin, RetrieveModelMixin, GenericAPIView):
    queryset = ComplaintAssignModel.objects.all()
    serializer_class = ComplaintAssignSerializer

    def post(self, request, *args, **kwargs):
        update = self.update(request, *args, **kwargs)
        if update:
            messages.success(request, "Assign Engineer has been updated successfully")
            return redirect('assign_complete')

    def get(self, request, *args, **kwargs):
        user = Users.objects.filter(user_dept="Installation").all()
        context = {
            'users': user,
            'department': 'Installation',
            "assign": "update",
            "data": self.get_object()
        }
        return render(request, "Complaints.html", context)
