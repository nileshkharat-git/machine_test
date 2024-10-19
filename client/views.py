from django.shortcuts import redirect
from rest_framework.views import APIView
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import Client

class ClientView(APIView):
    """API endpoint that allows clients to be viewed, created, updated or deleted by logged in user."""
    
    permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        """API endpoint that allows clients to be viewed by logged in user. specifically by id. If id is not provided, all clients are returned."""
        if id:
            client = Client.objects.get(id=id)
            serialize_client = ClientByIDSerializer(client)
            return Response(serialize_client.data)
        client = Client.objects.defer("projects")
        serialize_client = ClientSerializer(client, many=True)
        return Response(serialize_client.data)
    
    def post(self, request):
        """API endpoint that allows a client to be created."""
        try:
            client_name = request.data.get('client_name')
            created_by = request.user
            client = Client.objects.create(client_name=client_name, created_by=created_by)
            client.save()
            serialize_client = ClientSerializer(client)
            return Response(serialize_client.data)
        except Exception as e:
            return Response({"message": e.args[0]})
    
    def put(self, request, id):
        """API endpoint that allows a client to be updated."""
        try:
            client = Client.objects.get(id=id)
            client_name = request.data.get('client_name')
            client.client_name = client_name
            client.save()
            serialize_client = ClientUpdateSerializer(client)
            return Response(serialize_client.data)
        except Exception as e:
            return Response({"message": e.args[0]})
    
    def delete(self, request, id):
        """API endpoint that allows a client to be deleted."""
        client = Client.objects.get(id=id)
        client.delete()
        return Response({"message": "Client deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

#Logout view redirects to /clients. It is optional. Here we are just testing the logout functionality.
def logout_view(request):
    logout(request)
    return redirect('/clients')