from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    """Client Model to create clients.
    created_by: foreign key to User model
    projects: many to many relationship with Project model"""
    
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    projects = models.ManyToManyField('project.Project', blank=True, related_name='projects')
    
    def __str__(self):
        return self.client_name
    


