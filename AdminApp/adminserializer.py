from rest_framework.serializers import ModelSerializer
from .models import *

# user serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        # fields = ['id', 'name', 'email', 'password', 'user_dept', 'designation','work', 'is_active']