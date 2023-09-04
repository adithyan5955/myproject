
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from.models import Task
# Create your views here.
from django.shortcuts import render
from.forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class Tasklistview(ListView):
    model=Task
    template_name='home.html'
    context_object_name='task'

class TaskDetailView(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='task'

class TaskUpdateView(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model=Task
    template_name='delete.html'
    context_object_name='task'
    success_url = reverse_lazy('cbvhome')

    

def todo_page(request):
    tasks = Task.objects.order_by('priority')
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority,date=date)
        task.save()

    return render(request, 'home.html', {'task': tasks})

def details(request):
    task=Task.objects.all()
    return render(request, 'detail.html',{'task':task})

def deletetask(request, taskid):
    task = get_object_or_404(Task, id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('todo_page')  

    return render(request, 'delete.html', {'task': task})

def updatetask(request, id):
    task = get_object_or_404(Task, id=id)
    f = TodoForm(request.POST or None, instance=task)
    
    if request.method == 'POST':
        if f.is_valid():  # Validate the form before accessing cleaned_data
            f.save()
            return redirect('todo_page')
    
    return render(request, 'edit.html', {'f': f, 'task': task})