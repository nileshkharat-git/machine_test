from django.contrib import admin
from django.urls import path, include
from project.views import ProjectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("clients/", include("client.urls")),                      #url to include client app urls
    path("projects/", ProjectView.as_view()),                      #url to view all projects
]
