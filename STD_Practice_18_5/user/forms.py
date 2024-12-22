from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    first_name =forms.CharField(max_length=30)
    last_name =forms.CharField(max_length=30)
    email = forms.EmailField()
    phone =forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','phone','password1','password2']
        






