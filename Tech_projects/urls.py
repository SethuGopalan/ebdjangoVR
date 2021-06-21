from django.urls import path
from . import views

urlpatterns = [
    path("",views.Tech_project_index,name="Tech_project_index"),
    path("<int:key>/",views.Tech_project_details,name="Tech_project_details"),
]
