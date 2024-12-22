from django.shortcuts import render
from django.views.generic.list import ListView
from album.models import Album


class ContentView(ListView):
    model = Album
    template_name= "home.html"
    context_object_name = 'albums'
    
    def get_queryset(self):
        return Album.objects.all()