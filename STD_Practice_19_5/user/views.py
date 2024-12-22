from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    next_page = "home"


class RegisterView(FormView):
    template_name = "registration/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("home")
    
    def dispatch(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save();
        login(self.request,user)
        return super().form_valid(form)
    
    

# def register_view(request):
#     if request.user.is_authenticated:
#         return redirect("home")
#     if request.method =="POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             return redirect('home')
        
#     else:
#         form = UserRegisterForm()
        
#     return render(request,'registration/register.html',{'form': form})