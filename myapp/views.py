
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.


def index(request):
    return render(request, 'index.html')


def hello(request, username):
    return HttpResponse(f"Hello {username}")


def about(request):
    return HttpResponse('about')


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def tasks(request):
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })

    else:
        Task.objects.create(
            title=request.POST["title"], description=request.POST["description"], proyect_id=2,)
    return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_projects.html', {
            "form": CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(proyect_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })
