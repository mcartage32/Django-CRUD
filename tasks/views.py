from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

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


def signout(request):
    logout(request)
    return redirect('index')


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
