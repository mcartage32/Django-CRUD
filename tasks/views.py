from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'index.html')


def tasks(request):
    return render(request, 'tasks.html')


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
