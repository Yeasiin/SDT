from django import forms
from .models import Transaction
from accounts.models import UserBankAccount
from bank.models import BankState


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount','transaction_type']
        
    def __init__(self, *args, **kwargs):
        self.account  = kwargs.pop('account')
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()
        
    def save(self, commit = False):
        self.instance.account = self.account
        self.instance.balance_after_transaction  = self.account.balance
        return super().save()
    
class SendMoneyForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['linked_account', 'amount','transaction_type']
        
    def __init__(self, *args, **kwargs):
        self.account  = kwargs.pop('account')
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()
        
    def save(self, commit = False):
        self.instance.account = self.account
        self.instance.balance_after_transaction  = self.account.balance
        return super().save()
    
    def clean_amount(self):
        account = self.account
        max_sent_amount = 20000
        balance = account.balance 
        amount = self.cleaned_data['amount']
        
        if amount <=0:
            raise forms.ValidationError(f'Minimum amount is 1')
        
        if amount > max_sent_amount:
             raise forms.ValidationError(f'You can\' send more then {max_sent_amount} at once')

        if amount > balance:
            raise forms.ValidationError(f'You have {balance}$ in your account, you can\'t send more then your account balance ')

        return amount
    
    def clean_linked_account(self):
        linked_account = self.cleaned_data["linked_account"]
        if not UserBankAccount.objects.filter(account_no=linked_account).exists():
            raise forms.ValidationError(f'Account don\'t exists ')
        
        if self.account.account_no == linked_account:
             raise forms.ValidationError('You cannot send money to your own account.')
         
         
         
        return linked_account
    
    
class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get("amount")
        if amount < min_deposit_amount:
            raise forms.ValidationError(f'You need to deposit at least {min_deposit_amount}$')
        
        return amount
    

class WithDrawForm(TransactionForm):
    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance 
        amount = self.cleaned_data['amount']
        
        bank_state  = BankState.objects.first()
        
        if not bank_state.bank_operational:
            raise forms.ValidationError("The bank is bankrupt")
        
        if amount < min_withdraw_amount:
            raise forms.ValidationError(f'Minimum withdraw is {min_withdraw_amount}')
        
        if amount > max_withdraw_amount:
             raise forms.ValidationError(f'You can\' withdraw more then {min_withdraw_amount} at once')

        if amount > balance:
            raise forms.ValidationError(f'You have {balance}$ in your account, you can\'t withdraw more then your account balance ')

        return amount
    
    
class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        
        return amount
    
    
