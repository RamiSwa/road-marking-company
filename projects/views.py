from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language
from .models import Project

def project_list(request):
    """Display all projects"""
    language = get_language()
    projects = Project.objects.all()
    return render(request, "projects/project_list.html", {"projects": projects, "language": language})

def project_detail(request, project_id):
    """Display a single project with its gallery images"""
    language = get_language()
    project = get_object_or_404(Project, id=project_id)
    return render(request, "projects/project_detail.html", {"project": project, "language": language})
