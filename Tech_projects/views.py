from django.shortcuts import render

from Tech_projects.models import Tech_project

def Tech_project_index(request):
    Tech_projects = Tech_project.objects.all()
    context = {
        'Tech_projects' : Tech_projects
    }
    return render(request, 'Tech_project_index.html',context)

def Tech_project_details(request,key):
    tech_project = Tech_project.objects.get(key=key)
    context={
        'tech_project':tech_project
    }
    return render(request,'Tech_project_details.html',context)

     