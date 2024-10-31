from django.shortcuts import render,redirect
from .forms import MusicianModelForm
from .models import MusicianModel

# Create your views here.
def add(request):
    if request.POST:
        form = MusicianModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MusicianModelForm()
    
    return render(request, 'add_musician.html',{'form':form,})


def update(request,id):
    entry =  MusicianModel.objects.get(pk=id)
    form  = MusicianModelForm(instance=entry)
    
    if request.POST:
        form = MusicianModelForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect("home")
            
    return render(request, "update_musician.html",{'form':form})


def delete(request,id):
    entry = MusicianModel.objects.get(pk=id)
    entry.delete()
    return redirect("home")

