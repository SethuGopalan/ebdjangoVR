from django.urls import path
from . import views

urlpatterns = [
    path("", views.Tech_project_index, name="Tech_project_index"),
    path("", views.Tech_project_detail, name="Tech_project_detail"),
    path("<int:key>/", views.Tech_project_detail, name="Tech_project_detail"),
]
