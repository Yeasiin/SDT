from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import MusicianForm
from .models import Musician

# Create your views here.
# def create(request):
#     form = MusicianForm()
#     return render(request,'add_data.html',{'form':form,'form_name':"Musician"})

class CreateMusicianView(CreateView):
    model = Musician
    fields = "__all__"
    template_name = "add_data.html"
    success_url = reverse_lazy('home')  
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Musician'
        return context
        
        

class UpdateMusicianView(UpdateView):
    model = Musician
    fields = "__all__"
    template_name = "update_data.html"
    success_url = reverse_lazy("home")
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Musician'
        return context
        
        
        
class DeleteMusicianView(DeleteView):
    model = Musician
    template_name = "delete.html"
    success_url = reverse_lazy("home")