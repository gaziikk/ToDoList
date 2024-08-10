from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

def index(request):
    tasks = Task.objects.all()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()

    context = {
        'form': form,
        'tasks': tasks,
    }
    return render(request, 'index.html', context)

 