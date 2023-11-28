from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import Create_new_task, Create_new_project
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {'title':title})

def about(request):
    username = 'Marcos'
    return render(request, 'about.html',{'username':username})

def hello(request, username):
    print(username)
    return HttpResponse('Hello %s' % username)

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects':projects})

def task(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks':tasks})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {'form':Create_new_task()})
    else:
        Task.objects.create(title = request.POST['title'], description = request.POST['description'], project_id = 2)
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {'form':Create_new_project()})
    else:
        Project.objects.create(name = request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id = id)
    return render(request, 'projects/detail.html', {'project':project,'tasks':tasks})