from django.shortcuts import render, redirect
from .models import Task
from .forms import CreateTask
 
# Create your views here.
def home_view(request):
    tasks = Task.objects.all()
    return render(request,'tasks/home.html',{'tasks':tasks})

def create_view(request):
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:home')
    else:
        form = CreateTask()
    return render(request,'tasks/create.html',{'form':form})

def delete_view(request,pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('tasks:home')