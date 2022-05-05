from django.shortcuts import render, redirect
from rest_framework.generics import *
from rest_framework.mixins import *
from .models import *
from django.http import *
from django.views.generic.list import ListView
from Installation.models import *
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from SalesApp import *
from SalesApp.views import *
from AdminApp.views import *
from AdminApp import *
from .models import *
from Installation.models import *
from SalesApp.models import LeadModel

# Create your views here.
# display a page using tags
def OpenUser(request, tag):
    context = {
        'department': ""
    }
    if tag == 'openuser':
        return render(request, 'InventoryHome.html')
    # elif tag == 'opensaleshome':
    #     return redirect('client_details')
    

def Add_BOM(request): 
    return render(request, 'Add_BOM.html')

def InventoryHome(request):
    queryset = LeadModel.objects.all().order_by('-id')
    return render(request, 'InventoryHome.html')



class LeadListView(ListView):
    queryset = LeadModel.objects.all().order_by('-id')
    template_name = 'InventoryHome.html'
    context_object_name = 'leads'

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        context['department'] = 'Inventory'
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
