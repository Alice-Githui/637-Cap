from django import forms
from django.contrib.auth.models import User
from .models import Account, Transaction


class DepositFunds(forms.ModelForm):
    class Meta:
        model=Transaction
        # exclude=['user', 'recipient_account', 'recipient_name', 'account']
        fields=['amount']

class TransferFunds(forms.ModelForm):
    class Meta:
        model = Transaction
        fields =['recipient_name', 'account', 'amount']


class WithdrawFunds(forms.ModelForm):
    class Meta:
        model=Transaction
        # exclude=['user', 'recipient_account', 'recipient_name', 'account']
        fields=['amount']