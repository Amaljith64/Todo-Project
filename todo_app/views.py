from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ModeForm
from .models import task
from django.views.generic import ListView


# Create your views here.

class TaskListView(ListView):
    model = task
    template_name = 'task_view.html'
    context_object_name = 'obj1'

def task_view(request):
    obj1=task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date=request.POST.get('date')
        obj = task(name=name, priority=priority,date=date)
        obj.save()
    return render(request, 'task_view.html',{'obj1':obj1})

def delete(request,taskid):
    Task=task.objects.get(id=taskid)
    if request.method=='POST':
        Task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':Task})


def update(request,taskid):
    Task=task.objects.get(id=taskid)
    form=ModeForm(request.POST or None,instance=Task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':Task})




#
# def Task(request):
#
#     return render(request, '')


