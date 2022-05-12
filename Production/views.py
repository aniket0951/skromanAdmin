from django.shortcuts import render
from gc import get_objects
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from h11 import Data
from rest_framework.generics import *
from rest_framework.mixins import *
from django.contrib import messages
from AdminApp.models import *
from AdminApp.adminserializer import *
from django.views.generic.list import ListView
from SalesApp.models import LeadModel
from .models import *
# from .inst_serilizer import *
from django.db.models import Q
from datetime import date

from rest_framework.decorators import action,api_view
from common.Helper import  get_current_date, user_validation,get_timedelta_compare



# Create your views here.


def Production_Request(request): 
    return render(request, 'ProductionRequest.html')


class LeadListView(ListView):
    queryset = LeadModel.objects.all().order_by('id')
    template_name = 'ProductionHome.html'
    context_object_name = 'leads'

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        context['department'] = 'Production'
        search = self.request.GET.get('search')
        if search:
            data = self.get_queryset().filter(Q(name__icontains=search) | Q(contact__icontains=search)
                                              | Q(site_name__icontains=search) | Q(city__icontains=search)
                                              | Q(pin_code__icontains=search) | Q(ctime__icontains=search)) \
                .all()
            context.update({"leads": data})

        startdate = self.request.GET.get('startdate')
        enddate = self.request.GET.get('enddate')
        if startdate and enddate:
            data = self.get_queryset().filter(Q(ctime__date__range=(startdate, enddate))).all()
            context.update({"leads": data})

        return context


def OpenProduction(request, tag):
    # context = {'department': 'Installation'}
    if tag == 'adduser':
        return redirect('user_list')
    elif tag == 'addNewUser':
        context = {}
        context['department'] = 'Production'
        context['edit'] = 'addForm'
        return render(request, 'ProductionHome.html', context)
    if tag.work == 'production_admin':
        return redirect('lead_list')
    elif tag.work == 'production_user':
        return redirect('production_user', pk=tag.id)    
    else:
        return HttpResponse(f"no matched tag {tag.work}")


class ProductionUser(CreateModelMixin, RetrieveModelMixin, GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        add = self.create(request, *args, **kwargs)
        if add:
            messages.success(request, "New User Addedd Successfully.")
            return redirect('user_list')
    
    def get(self, request, *args, **kwargs):
        data = self.retrieve(request, *args, **kwargs)
        return render(request, "ProductionHome.html", {"data": data})




