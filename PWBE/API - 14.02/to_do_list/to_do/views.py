from django.shortcuts import render
from .models import Task

# Create your views here.
def tasks(request):
    tasks = Task.objects.all().order_by('-titulo')
    return render(request, 'to_do/tasks.html', {'tasks':tasks})
