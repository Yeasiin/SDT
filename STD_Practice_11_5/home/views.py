from django.shortcuts import render
from utils.content import meals

# Create your views here.
def index(request):
    return render(request,'index.html',{'data': meals})