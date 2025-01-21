from django.contrib import admin
from django.urls import path, include
from .views import UserRegistrationView,UserLoginView, UserLogoutView, UserBankAccountUpdateView, ChangeUserPassword

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(),name='registration'),
    path("login/", UserLoginView.as_view(), name='login'),
    path("logout/",UserLogoutView.as_view(), name="logout" ),
    path("profile/",UserBankAccountUpdateView.as_view(), name="profile"),
    path("profile/change_password", ChangeUserPassword.as_view(),name="change_password")
]
