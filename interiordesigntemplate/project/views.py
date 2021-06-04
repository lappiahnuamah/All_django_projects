from django.shortcuts import render, get_object_or_404
from .models import Project
from .forms import ProjectFilter


# Create your views here.
def all_project(request):
    projects = Project.objects.all()
    filtered = ProjectFilter(request.GET, queryset=projects)
    projects = filtered.qs
    context = {
        'projects':projects,
        'filtered': filtered,
    }
    return render(request, 'all_project.html', context)


def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project':project
    }
    return render(request, 'detail.html', context)