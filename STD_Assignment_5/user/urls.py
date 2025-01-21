from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
     path("deposit/",views.DepositView.as_view(),name="deposit"),
     path("login/", views.UserLoginView.as_view(), name='login'),
     path('logout/',LogoutView.as_view(), name='logout'),
     path("register/",views.RegisterView.as_view(),name="register")
]
