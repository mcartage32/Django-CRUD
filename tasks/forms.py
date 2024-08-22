from django import forms
from django.forms import ModelForm
from .models import Task


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write description'}),
            'datecompleted': forms.DateInput(attrs={'type': 'date'})
        }


class UpdateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'datecompleted', 'important']
        widgets = {
            'datecompleted': forms.DateInput(attrs={'type': 'date'})
        }
