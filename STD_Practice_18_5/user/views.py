from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from user.forms import UserRegistrationForm

# Create your views here.

def user_logout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect("home")


def user_login(request):
    if(request.method =="POST"):
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate( request,username=username, password=password)
        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect("login")
        else:
            messages.success(request, "Logged In Successfully")
            login(request,user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html",{'form':form})


def register_user(request):
    if request.method =="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user =  form.save()
            messages.success(request,"Your account has been created!")
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"Failed to create account")
    else:
        form = UserRegistrationForm()
        
    return render(request,"registration/register.html", {'form':form})



def change_password(request):
    if request.method == "POST":
        form =PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,"Password changed successful!")
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request,"change-password.html",{'form':form})

def password_reset(request):
    if request.method =="POST":
        form  = SetPasswordForm(user=request.user,data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password reset successful!")
            return redirect("profile")
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, "change-password.html", {'form':form})




