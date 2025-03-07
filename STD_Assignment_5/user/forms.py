
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    first_name =forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','phone','password1','password2']
 


class CustomUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in self.fields:
            del self.fields['password']
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        exclude = ['password']







class DepositForm(forms.Form):
    balance = forms.IntegerField(label='Deposit Amount')
    
    def clean_balance(self):
        balance = self.cleaned_data['balance']
        if not balance >1:
            raise ValidationError("amount is too low!")
        
        return balance
        
    
    

