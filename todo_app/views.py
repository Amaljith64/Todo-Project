from django.http import HttpResponse
from django.shortcuts import render
from .models import task


# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        obj = task(name=name, priority=priority)
        obj.save()
    return render(request, 'home.html')
