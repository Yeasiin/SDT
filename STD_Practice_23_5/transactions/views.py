from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .constants import DEPOSIT, LOAN, LOAN_PAID,WITHDRAW, SEND_MONEY, RECEIVED_MONEY
from .models import Transaction
from .forms import DepositForm, WithDrawForm, LoanRequestForm, SendMoneyForm
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Sum
from accounts.models import UserBankAccount
from transactions.models import Transaction
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string



def send_transactional_email(mail_sub,template_name,to_user,amount,user):
    message = render_to_string(template_name,{'amount':amount, 'user':user})
    send_email = EmailMultiAlternatives(mail_sub,"",to=[to_user])
    send_email.attach_alternative(message,"text/html")
    send_email.send()
    


# Create your views here.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transaction_report')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'account':self.request.user.account})
        return kwargs 
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title':self.title})
        return context
    
class DepositMoneyView(TransactionCreateMixin):
    title = "Deposit"
    form_class = DepositForm
    
    def get_initial(self):
        initial = {'transaction_type':DEPOSIT}
        return initial
    
    def form_valid(self, form):
        if form.is_valid():
            amount = form.cleaned_data.get("amount")
            account = self.request.user.account
            account.balance += amount
            account.save(update_fields=['balance'])
            
            messages.success(self.request, f'{amount}$ was deposited to your account successfully')
        
        
                
        send_transactional_email(mail_sub='Deposit message',
                                 template_name='deposit_email.html',
                                 to_user=self.request.user.email,
                                 amount=amount, user=self.request.user)
        
        
    
     
        
  
   
        return super().form_valid(form)


class WithdrawMoneyView(TransactionCreateMixin):
    title = "Withdraw Money"
    form_class = WithDrawForm
    
    def get_initial(self):
        initial = {'transaction_type':WITHDRAW}
        return initial
    
    def form_valid(self, form):
        if form.is_valid():
            
            amount = form.cleaned_data.get("amount")
            account = self.request.user.account
            account.balance -= amount
            account.save(update_fields=['balance'])
            
            messages.success(self.request, f'Successfully Withdrawn {amount}$ from your account')
        
        send_transactional_email(mail_sub='Withdraw message',
                                 template_name='withdraw_email.html',
                                 to_user=self.request.user.email,
                                 amount=amount, user=self.request.user)
        
        return super().form_valid(form)
    
class LoanRequestView(TransactionCreateMixin):
    title = "Request For Loan"
    form_class = LoanRequestForm
    
    def get_initial(self):
        initial = {'transaction_type':LOAN}
        return initial
    
    def form_valid(self, form):
        if form.is_valid():
            amount = form.cleaned_data.get("amount")
            current_loan_count = Transaction.objects.filter(account = self.request.user.account, transaction_type=LOAN, loan_approve=True).count()
            if current_loan_count >= 3:
                return HttpResponse('You have crossed your limits')
            
            messages.success(self.request,f'Loan request for {amount} has been successfully sent to admin')
            
        send_transactional_email(mail_sub='Loan message',
                                 template_name='loan_request_email.html',
                                 to_user=self.request.user.email,
                                 amount=amount, user=self.request.user)
            
            
        return super().form_valid(form)
    
class TransactionReportView(LoginRequiredMixin,ListView):
    template_name = "transaction_report.html"
    model  = Transaction
    balance  = 0
    
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(account = self.request.user.account)
        
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')
        
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str,"%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str,"%Y-%m-%d").date()
        
            queryset= queryset.filter(timestamp__date__gte=start_date, timestamp__date__lte = end_date)
            
            self.balance = Transaction.objects.filter(timestamp__date__gte=start_date, timestamp__date__lte = end_date).aggregate((Sum('amount')))['amount__sum']
            
        else:
            self.balance = self.request.user.account.balance
            
        return queryset
        
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'account':self.request.user.account})
        return context
    

class PayLoanView(LoginRequiredMixin,View):
    def get(self,request,loan_id):
        loan = get_object_or_404(Transaction,id=loan_id)
        
        if loan.loan_approve:
            user_account  = loan.account
            if loan.amount < user_account.balance:
                user_account.balance -= loan.amount
                loan.balance_after_transaction = user_account.balance
                user_account.save()
                loan.transaction_type = LOAN_PAID
                loan.save() 
                return redirect('loan_list')
            else:
                messages.error(self.request, f"Loan Amount is getter then available balance")
                return redirect('loan_list')
            
class LoanListView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = "loan_request.html"
    context_object_name = 'loans'
    
    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transaction.objects.filter(account = user_account, transaction_type = LOAN )
        return queryset
    
    
class SendMoneyView(TransactionCreateMixin):
    form_class = SendMoneyForm
    template_name = 'send_money_form.html'
    title = "Send Money"

    def get_initial(self):
        initial = {'transaction_type':SEND_MONEY}
        return initial
    
    def form_valid(self, form):
        if form.is_valid():
            amount = form.cleaned_data.get("amount")
            linked_account = form.cleaned_data.get("linked_account")
            account = self.request.user.account
            account.balance -= amount
            account.save(update_fields=['balance'])
            
            
            other_acount = UserBankAccount.objects.filter(account_no=linked_account).first()

            other_acount.balance +=amount
                
            receive_transaction = Transaction(
                account=other_acount,
                amount = amount,
                balance_after_transaction = other_acount.balance,
                transaction_type = RECEIVED_MONEY,
                linked_account=self.request.user.account.account_no)

            receive_transaction.account.balance = other_acount.balance
            receive_transaction.account.save(update_fields=['balance'])
            receive_transaction.save()
            
            messages.success(self.request, f'{amount} sent Yeasin\'s account')
            
            send_transactional_email(mail_sub='Money sent message',
                                 template_name='money_sent_email.html',
                                 to_user=self.request.user.email,
                                 amount=amount, user=self.request.user)
            
            send_transactional_email(mail_sub='Money Receive message',
                                 template_name='money_receive_email.html',
                                 to_user=other_acount.user.email,
                                 amount=amount, user=other_acount.user)
        
        
        
        
        return super().form_valid(form)
    
    
    
    
    
    