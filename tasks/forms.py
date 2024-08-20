from django import forms
from django.forms import ModelForm
from .models import Task


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['tittle', 'description', 'important']


class UpdateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['tittle', 'description', 'datecompleted', 'important']
        widgets = {
            'datecompleted': forms.DateInput(attrs={'type': 'date'})
        }
