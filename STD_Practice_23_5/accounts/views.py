from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView, View,UpdateView
from django.contrib.auth.views import LoginView, LogoutView,PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm
from transactions.views import send_transactional_email


# Create your views here.
class UserRegistrationView(FormView):
    template_name= "user_registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("index")
    
    def form_valid(self,form):
        user  = form.save()
        login(self.request,user)
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name = "user_login.html"
    def get_success_url(self):
        return reverse_lazy('index')
    


class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy("index")

class ChangeUserPassword(PasswordChangeView):
    template_name = 'change_password.html'
    form_class= PasswordChangeForm
    success_url = reverse_lazy("profile")
    
    def form_valid(self, form):
        print("--x--x--")
        send_transactional_email(mail_sub="Password change message", template_name="password_change_email.html",amount=0, to_user=self.request.user.email,user=self.request.user)
        messages.success(self.request, "Password Change Successful")
        form.save()
        return super().form_valid(form)


class UserBankAccountUpdateView(View):
    template_name = 'profile.html'
    
    def get(self,request):
        form  = UserUpdateForm(instance = request.user)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form =  UserUpdateForm(request.POST, instance = request.user)
        
        if form.is_valid():
            form.save()
            return redirect("index")
        
        return render(request, self.template_name, {'form':form})
    
    
    
    






