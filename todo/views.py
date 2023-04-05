from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def todos(request):
    #tasks = Task.objects.get(user_id=request.user.id)
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/to_do_database')
    
    completedTasks = True
    for t in tasks:
        if t.complete == False:
            completedTasks = False
    
    context = {
        'tasks': tasks, 
        'form': form,
        'completedTasks': completedTasks, 
        "breadcrumb":
            {"parent":"Todo", "child":"Todo with database"}
        }
    
    return render(request,'todo/todo.html',context)
    
