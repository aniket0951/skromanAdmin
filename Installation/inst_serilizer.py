from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import *
from SalesApp.salesSerializer import LeadSerializer


class ComplaintSerializer(ModelSerializer):
    lead = LeadSerializer(many=True, read_only=True)
    class Meta:
        model = ComplaintsModel
        fields = '__all__'

class ComplaintAssignSerializer(ModelSerializer):
    complaint = ComplaintSerializer(many=True, read_only=True)
    assignee = ComplaintSerializer(many=True, read_only=True)
    class Meta:
        model = ComplaintAssignModel
        fields = '__all__'