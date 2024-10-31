from django.shortcuts import render
from album.models import AlbumModel


def index(request):
    entries = AlbumModel.objects.all()
    
    print(entries,"hello")    
    
    return render(request,'home.html',{'data':entries})