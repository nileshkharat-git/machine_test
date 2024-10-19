from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """Project model to create projects for clients."""
    
    project_name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, blank=True)
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name