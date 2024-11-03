from django.shortcuts import render
from task.models import TaskModel

def index(request):    
    data = TaskModel.objects.all()
    return render(request,"index.html",{'data':data})