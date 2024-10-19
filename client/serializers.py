from rest_framework import serializers
from .models import Client
from project.serializers import ProjectForClientSerializer

class ClientSerializer(serializers.ModelSerializer):
    """Serializer to map the Client Model instance into JSON format."""
    
    created_by = serializers.CharField(source='created_by.username')
    class Meta:
        model = Client
        exclude = ['updated_at','projects']
        ordering = ['-created_at']

class ClientByIDSerializer(serializers.ModelSerializer):
    """Serializer to map the Client Model instance by id into JSON format."""
    
    projects = ProjectForClientSerializer(many=True)
    created_by = serializers.CharField(source='created_by.username')
    class Meta:
        model = Client
        fields = '__all__'

class ClientUpdateSerializer(serializers.ModelSerializer):
    """Serializer to map the Client Model instance into JSON format after update. Exclude the projects field."""
    created_by = serializers.CharField(source='created_by.username')
    class Meta:
        model = Client
        exclude = ['projects']
