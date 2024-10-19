from rest_framework import serializers
from .models import Project
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    """ Serializer to map the User Model instance into JSON format. """
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    """ Serializer to map the Project Model instance into JSON format.  Exclude the updated_at field. """
    created_by = serializers.CharField(source='created_by.username')
    client = serializers.CharField(source='client.client_name')
    users = UserSerializer(many=True)
    class Meta:
        model = Project
        exclude = ['updated_at']

class ProjectForUserSerializer(serializers.ModelSerializer):
    """ Serializer to map the Project Model instance into JSON format. It is used for the user view. """
    created_by = serializers.CharField(source='created_by.username')
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'created_by', 'created_at']
        
class ProjectForClientSerializer(serializers.ModelSerializer):
    """ Serializer to map the Project Model instance into JSON format. It is used for the client view. """
    class Meta:
        model = Project
        fields = ['id', 'project_name']