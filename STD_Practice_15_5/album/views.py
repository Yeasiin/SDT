from django.shortcuts import render,redirect
from .forms import AlbumModelForm
from .models import AlbumModel

# Create your views here.

def add(request):
   if(request.POST):
      form = AlbumModelForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("home")
   else:
      form = AlbumModelForm()

   return render(request, 'add_album.html',{'form':form})


def update(request,id):
   album = AlbumModel.objects.get(pk=id)
   form = AlbumModelForm(instance=album)
   if(request.POST):
      form = AlbumModelForm(request.POST, instance=album)
      if form.is_valid():
         form.save()
         return redirect("home")

   return render(request,"update_album.html",{'form':form})
   



