from django.contrib import admin
from django.urls import path, include
from .views import DepositMoneyView,LoanListView,LoanRequestView,PayLoanView,WithdrawMoneyView,TransactionReportView, SendMoneyView

urlpatterns = [
    path('deposit/', DepositMoneyView.as_view(), name='deposit_money'),
    path('report/', TransactionReportView.as_view(), name='transaction_report'),
    path('withdraw/', WithdrawMoneyView.as_view(), name='withdraw_money'),
    path('loan_request/', LoanRequestView.as_view(), name='loan_request'),
    path('loans/', LoanListView.as_view(), name='loan_list'),
    path('pay/<int:loan_id>/',PayLoanView.as_view(), name='pay_loan'),
    path('send_money/',SendMoneyView.as_view(), name="send_money")
]
