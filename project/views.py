from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Project
from .serializers import *
from client.models import Client


class ProjectView(APIView):
    
    """API endpoint that allows projects to be viewed or create."""
    
    def get(self, request):
        """API endpoint that allows projects to be viewed by logged in user."""
        projects = Project.objects.filter(users=request.user)
        serialize_project = ProjectForUserSerializer(projects, many=True)
        return Response(serialize_project.data)
    

    def post(self, request, client_id=None):
        """API endpoint that allows a project to be created."""
        try:
            project_name = request.data.get('project_name')
            created_by = request.user
            client = Client.objects.get(id=client_id)
            users = request.data.get('users')

            project = Project.objects.create(project_name=project_name, client=client, created_by=created_by)
            project.save()
            
            for user in users:
                user = User.objects.get(id=user['id'])
                project.users.add(user)

            project.save()
            client.projects.add(project)
            client.save()
            serialize_project = ProjectSerializer(project)
            return Response(serialize_project.data)
        except Exception as e:
            return Response({"message": e.args[0]})