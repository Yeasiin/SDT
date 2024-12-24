from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.views.generic import FormView, UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserRegisterForm, CustomUserChangeForm
from django.contrib.auth.models import User

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
    


class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = "update_user.html"
    success_url = reverse_lazy("home")
    
    def get_object(self, queryset =None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, "Your profile has been updated successfully.")
        return super().form_valid(form)
    
    



