from rest_framework.serializers import ModelSerializer
from .models import *
from Installation.models import *



# client model from installation model
class ClientSerializer(ModelSerializer):
    class Meta:
        model = SkromanClients
        fields = '__all__'

# lead notes 
class LeadNoteSerializer(ModelSerializer):
    # leaddetails = LeadSerializer(many=True, read_only=True)
    class Meta:
        model = LeadNotes
        fields = '__all__'

# lead serializer from sales app model
class LeadSerializer(ModelSerializer):
    leaddetails = LeadNoteSerializer(many=True, read_only=True)
    class Meta:
        model = LeadModel
        fields = '__all__'