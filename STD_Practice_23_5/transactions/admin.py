from django.contrib import admin
from .models import Transaction
from .views import send_transactional_email

# Register your models here.
# admin.site.register(Transaction)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account','amount','balance_after_transaction','transaction_type','loan_approve']
    
    def save_model(self,request,obj,form,change):
        if obj.loan_approve == True:
            obj.account.balance += obj.amount
            obj.balance_after_transaction =  obj.account.balance
            obj.account.save()
            
        send_transactional_email(mail_sub='Loan approved message',
                                 template_name='loan_approved_email.html',
                                 to_user=obj.account.user.email,
                                 amount=0, user=obj.account.user)
            
        return super().save_model(request,obj,form,change)

