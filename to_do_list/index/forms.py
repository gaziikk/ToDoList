from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    
    task = forms.CharField(label='Задача', max_length=200)

    class Meta:
        model = Task
        fields = ("task",)
