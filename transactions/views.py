from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Account, Transaction
from .forms import *
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

# Create your views here.

class HomeView(ListView):
    model = Account
    template_name ='transactions/index.html'


class TransactionView(DetailView):
    model=Account
    template='transactions/maketransaction.html'


def deposit_funds(request, pk):
    form = DepositFunds
    account = Account.objects.get(id=pk)
    account_balance = account.account_balance
    # print(account_balance)

    if request.method=="POST":
        form=DepositFunds(request.POST)
        if form.is_valid():
            new_amount = form.cleaned_data.get('amount')
            # print(new_amount)
            new_account_balance = int(account_balance) + int(new_amount)
            account.account_balance = new_account_balance
            account.save()
           
        return redirect('home')

    else:
        form=DepositFunds()
    return render(request, 'transactions/maketransaction.html', {"form":form, "account":account})

def transfer_funds(request, pk):
    form = TransferFunds
    account = Account.objects.get(id = pk)
    account_balance = account.account_balance

    if request.method=="POST":
        form=TransferFunds(request.POST)
        if form.is_valid():
            new_amount = form.cleaned_data.get('amount')
            recipient = form.cleaned_data.get('account')
            # print(recipient)
            recipient_account = Account.objects.get(account_name = recipient)
            print(recipient_account)
            if account_balance < new_amount:
                return HttpResponse('You do not have sufficient funds to make this transfer')
            else:
                new_account_balance = int(account_balance) - int(new_amount)
                account.account_balance = new_account_balance
                account.save()

            # add to recipient
            recipient_balance = recipient_account.account_balance
            received_amount = form.cleaned_data.get('amount')
            updated_balance = int(recipient_balance) + int(received_amount)
            recipient_account.account_balance = updated_balance
            recipient_account.save()
           
        return redirect('home')

    else:
        form=TransferFunds()
    return render(request, 'transactions/transferfunds.html', {"form":form, "account":account})

def withdraw_funds(request, pk):
    form = WithdrawFunds
    account = Account.objects.get(id=pk)
    account_balance = account.account_balance
    # print(account_balance)

    if request.method=="POST":
        form=WithdrawFunds(request.POST)
        if form.is_valid():
            new_amount = form.cleaned_data.get('amount')
            # print(new_amount)
            if account_balance < new_amount:
                return HttpResponse('You do not have sufficient funds to make this withdrawal')
            else:
                new_account_balance = int(account_balance) - int(new_amount)
                account.account_balance = new_account_balance
                account.save()
           
        return redirect('home')

    else:
        form=WithdrawFunds()
    return render(request, 'transactions/withdrawfunds.html', {"form":form, "account":account})

    