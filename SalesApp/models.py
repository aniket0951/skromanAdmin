from django.db import models
from AdminApp.models import *
from Installation.models import *


# leads model class
class LeadModel(models.Model):
    lead_type = models.CharField(max_length=40, null=True, blank=True)
    leads = models.CharField(max_length=40, null=True, blank=True)
    name = models.CharField(max_length=40, null=True, blank=True)
    contact = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField(max_length=254)
    ctime = models.DateTimeField(auto_now_add=True) 
    uptime = models.DateTimeField(auto_now=True)
    billing_address = models.CharField(max_length=140, null=True, blank=True)
    shipping_address = models.CharField(max_length=140, null=True, blank=True)
    note_comment = models.CharField(max_length=400, null=True, blank=True)
    next_followup = models.CharField(max_length=60, null=True, blank=True)
    sales_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='users')
    lead_id = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    status_lead = models.CharField(max_length=10, null=True, blank=True)
    pin_code = models.CharField(max_length=40, null=True, blank=True)
    lead_status = models.CharField(max_length=40, null=True, blank=True)
    client = models.ForeignKey(SkromanClients, on_delete=models.CASCADE, related_name="client")
    site_name = models.CharField(max_length=255, null=True, blank=True)
    ref_type = models.CharField(max_length=255, null=True, blank=True)
    ref_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'leads'


class LeadNotes(models.Model):
    note_comment = models.TextField(blank=True, null=True)
    next_followup = models.CharField(max_length=120, null=True, blank=True)
    is_demo = models.IntegerField(blank=True, null=True)
    is_site_visit = models.IntegerField(blank=True, null=True)
    is_electric_layout = models.IntegerField(blank=True, null=True)
    is_proposal = models.IntegerField(blank=True, null=True)
    is_lead_conform = models.IntegerField(blank=True, null=True)
    discount = models.CharField(max_length=20, null=True, blank=True)
    lead_id = models.ForeignKey(LeadModel, on_delete=models.CASCADE, related_name='leaddetails')
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lead_notes'
