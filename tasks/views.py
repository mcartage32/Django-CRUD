from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from tasks.models import Task
from .forms import CreateTaskForm, UpdateTaskForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html')

# REGISTRO


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {
            "form": UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                login(request, user)
                user.save()
                return redirect('tasks')
            except:
                return render(request, "signup.html", {
                    "error": "Error al crear el usuario",
                    "form": UserCreationForm
                })
        else:
            return render(request, "signup.html", {
                "error": "Las contraseñas no coinciden",
                "form": UserCreationForm
            })

# LOGUEO


def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password']
                            )
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': "User or password incorrect"
            })
        else:
            login(request, user)
            return redirect('tasks')

# LOGOUT


def signout(request):
    logout(request)
    return redirect('index')


@login_required
def tasks(request):
    return render(request, 'tasks.html', {
        'tasks': Task.objects.filter(user=request.user)
    })


@login_required
def createtask(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {
            'form': CreateTaskForm
        })
    else:
        try:
            form = CreateTaskForm(request.POST)
            auxForm = form.save(commit=False)
            auxForm.user = request.user
            auxForm.save()
            return redirect('tasks')
        except:
            return render(request, 'create_task.html', {
                'form': CreateTaskForm,
                'error': 'Failed Insert Task'
            })

# Ver detalle y actualizar


@login_required
def taskdetail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == "GET":
        form = UpdateTaskForm(instance=task)
        return render(request, 'task_detail.html', {
            'task': task,
            'form': form
        })
    else:
        try:
            form = UpdateTaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except:
            return render(request, 'task_detail.html', {
                'task': task,
                'form': form,
                'error': 'Error updating task'
            })


@login_required
def deletetask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('tasks')
