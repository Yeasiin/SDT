from django.shortcuts import render
from .forms import ExampleForm 

# Create your views here.
def index(request):
    form = ExampleForm()
    return render(request,"index.html",{'form':form })