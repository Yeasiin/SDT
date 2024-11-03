from django.shortcuts import render,redirect
from .forms import TaskModelForm
from .models import TaskModel

# Create your views here.
def add(request):
    form = TaskModelForm()
    
    if(request.POST):
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
            
    return render(request,"add_task.html",{'form':form})


def update(request,id):
    task = TaskModel.objects.get(pk = id)
    form = TaskModelForm(instance=task)
    
    if(request.POST):
        form = TaskModelForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
             
    return render(request,"update_task.html",{'form':form})

def delete(request,id):
    task = TaskModel.objects.get(pk = id)
    task.delete()
    return redirect("home")
   
        
    
    
    
    

