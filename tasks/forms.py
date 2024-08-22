from django import forms
from django.forms import ModelForm
from .models import Task


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']


class UpdateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'datecompleted', 'important']
        widgets = {
            'datecompleted': forms.DateInput(attrs={'type': 'date'})
        }
