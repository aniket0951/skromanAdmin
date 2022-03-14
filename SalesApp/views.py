from django.shortcuts import render, redirect
from rest_framework.generics import *
from rest_framework.mixins import *
from .salesSerializer import *
from .models import *
from django.http import *
from django.views.generic.list import ListView
from Installation.models import *
from django.contrib import messages
from django.http import HttpResponse, JsonResponse


# Create your views here.
def OpenUserModes(request, tag):
    context = {
        'department': ""
    }
    if tag == 'openmode':
        return render(request, 'UserMode.html')
    elif tag == 'opensaleshome':
        return redirect('client_details')
    elif tag == 'opennewclient':
        context.update({'department': 'Sales'})
        return render(request, 'AddNewClient.html', context)
    elif tag == 'openaddlead':
        context.update({'department': 'Sales'})
        context['skip'] = 'skips'
        return render(request, 'AddLead.html', context)
    elif tag == 'openleadpresentation':
        context.update({'department': 'Sales'})
        context['skip'] = 'skip'
        return render(request, 'AddLead.html', context)
    elif tag == 'openpresentation':
        context.update({'department': 'Sales'})
        context['skip'] = 'skip'
        context['presentation'] = 'presentation'
        return render(request, 'AddLead.html', context)

    # create a new lead or add an new lead


class LeadClass(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = LeadModel.objects.all()
    serializer_class = LeadSerializer

    def post(self, request, *args, **kwargs):
        sales_user = self.request.POST.get('sales_user')
        # sales_user = 1
        # return HttpResponse(sales_user)
        insert = self.create(request, *args, **kwargs)
        if insert:
            messages.success(self.request, 'New Lead Added Successfully')
            return redirect('leaddetails/')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class LeadUpdate(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = LeadModel.objects.all()
    serializer_class = LeadSerializer

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            lead_type = self.request.POST.get('lead_type')
            leads = self.request.POST.get('leads')
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            contact = self.request.POST.get('contact')
            billing_address = self.request.POST.get('billing_address')
            shipping_address = self.request.POST.get('shipping_address')
            city = self.request.POST.get('city')
            pin_code = self.request.POST.get('pin_code')
            lead_id = self.request.POST.get('lead_id')
            ref_type = self.request.POST.get('ref_type')
            ref_name = self.request.POST.get('ref_name')

            data = LeadModel.objects.filter(id=lead_id).update(lead_type=lead_type,
                                                               leads=leads, name=name, email=email,
                                                               contact=contact, billing_address=billing_address,
                                                               shipping_address=shipping_address, city=city,
                                                               pin_code=pin_code, ref_type=ref_type, ref_name=ref_name)
            if data:
                messages.success(self.request, 'Lead update successfully')
                return redirect('leadhome')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class LeadListView(ListView):
    queryset = LeadModel.objects.all().order_by('-id')
    template_name = 'Leads.html'
    context_object_name = 'leads'

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        context['department'] = 'Sales'

        return context


class ClientClass(CreateModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = SkromanClients.objects.all()
    serializer_class = ClientSerializer

    def post(self, request, *args, **kwargs):
        insert = self.create(request, *args, **kwargs)
        if insert:
            messages.success(self.request, 'New client added successfully')
            return redirect('client_details')


class EditClientClass(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = SkromanClients.objects.all()
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs):
        print('get fun called')
        context = {
            'data': self.get_object(),
            'request': 'edit',
            'department': 'Sales'
        }
        return render(request, 'AddNewClient.html', context)

    def post(self, request, *args, **kwargs):
        update = self.update(request, *args, **kwargs)
        if update:
            messages.success(self.request, 'Client information updated successfully')
            return redirect('client_details')


class ClientListView(ListView):
    queryset = SkromanClients.objects.all().order_by('-id')
    template_name = 'SalesHome.html'
    context_object_name = 'client_data'

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        context['department'] = 'Sales'

        return context


class LeadNoteClass(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericAPIView):
    queryset = LeadNotes.objects.all()
    serializer_class = LeadNoteSerializer

    # queryset = LeadModel.objects.all()
    # serializer_class = LeadSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        insert = self.create(request, *args, **kwargs)
        if insert:
            messages.success(self.request, 'New Lead Note Added Successfully')
            return redirect('leadhome')
        else:
            return HttpResponse('Failed to add note, try agian')


class LeadNotes(ListView):
    queryset = LeadNotes.objects.all()
    template_name = 'LeadNotes.html'
    context_object_name = 'lead'

    def get_context_data(self, **kwargs):
        context = super(LeadNotes, self).get_context_data(**kwargs)
        data = LeadNoteSerializer(self.queryset, many=True)
        lead_id = self.kwargs['pk']
        context['lead_note'] = self.queryset.filter(lead_id=lead_id)
        context['department'] = 'Sales'
        context['lead_id'] = lead_id
        return context


def SkromanVideo(request):
    return render(request, 'SkromanVideo.html')


def DeviceImages(request):
    return render(request, 'Device-Images.html')
