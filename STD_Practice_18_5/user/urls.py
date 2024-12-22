from django.contrib.auth import views as authView
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path("register/", views.register_user,name="register"),
    path("change-password/",views.change_password,name="change-password"),
    path("password-reset/",views.password_reset,name="password-reset")
]
