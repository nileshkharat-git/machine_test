from django.urls import path, re_path
from . import views
import project.views as project_views

urlpatterns = [
    path("", views.ClientView.as_view()),                                       #url to view all clients
    path("<int:id>", views.ClientView.as_view()),                               #url to view client by id
    path("projects", project_views.ProjectView.as_view()),                      #url to view all projects by logged in user
    path("<int:client_id>/projects", project_views.ProjectView.as_view()),      #url to view all projects by client id
    path("logout", views.logout_view),                                          #url to logout
]