from django.shortcuts import render,redirect
from .forms import CategoryModelForm

# Create your views here.
def add(request):
    form = CategoryModelForm()
    
    if request.POST:
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    
    return render(request,"add_category.html",{'form':form})