from pyexpat import model
from django.db import models
from AdminApp.models import *


# Create your models here.
class SkromanClients(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    c_type = models.CharField(max_length=60, null=True, blank=True)
    email = models.CharField(max_length=60, null=True, blank=True)
    contact = models.CharField(max_length=60, null=True, blank=True)
    address = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    pin_code = models.CharField(max_length=60, null=True, blank=True)
    sales_user = models.CharField(max_length=1000, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'clients'


class ComplaintsModel(models.Model):
    complaint_des = models.TextField()
    appointment_date = models.DateField()
    timeslot = models.CharField(max_length=120, null=True, blank=True)
    device = models.CharField(max_length=120, null=True, blank=True)
    lead_id = models.ForeignKey('SalesApp.LeadModel', on_delete=models.CASCADE, related_name="lead")
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)
    complaint_status = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'complaints'


# complaint assign
class ComplaintAssignModel(models.Model):
    complaint_id = models.ForeignKey(ComplaintsModel, on_delete=models.CASCADE, related_name="complaint")
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="assignee")
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'complaint_assign'

# assigned users
class AssignedUsers(models.Model):
    complaint_assign_id = models.ForeignKey(ComplaintAssignModel, on_delete=models.CASCADE, related_name="complaint_assigned")
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="assignee_user")
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'assigned_users' 
