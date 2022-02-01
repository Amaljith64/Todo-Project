from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import task


# Create your views here.

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





#
# def Task(request):
#
#     return render(request, '')


