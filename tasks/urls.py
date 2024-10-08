from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('tasks', views.tasks, name='tasks'),
    path('logout', views.signout, name='logout'),
    path('accounts/login/', views.signin, name='login'),
    path('create-task', views.createtask, name='create-task'),
    path('task-detail/<int:task_id>', views.taskdetail, name='task-detail'),
    path('task-delete/<int:task_id>', views.deletetask, name='task-delete'),
]
