from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import AlbumForm 
from . models import Album

# Create your views here.
def create(request):
    form = AlbumForm()
    return render(request, "add_data.html",{'form':form, 'form_name':"Album"})



class CreateAlbumView(CreateView):
    model = Album
    fields = ["name","musician","rating"]
    
    template_name = "add_data.html"
    success_url = reverse_lazy('home')  
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Album'
        return context
    
   
class UpdateAlbumView(UpdateView):
    model = Album
    fields  = ['name', 'musician','rating']
    template_name = 'update_data.html'
    success_url = reverse_lazy("home")
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Album'
        return context


class DeleteAlbumView(DeleteView):
    model = Album
    template_name = "delete.html"
    success_url = reverse_lazy("home")

