from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length= 300)
    email=models.CharField(max_length=400)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Account(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    account_name=models.CharField(max_length=255, null=True)
    acc_number=models.CharField(max_length=10, blank=True, editable=True, null=True)
    account_balance=models.IntegerField(default=0)


    def __str__(self):
        return self.account_name


class Transaction(models.Model):
	recipient_account = models.CharField(max_length=255)
	recipient_name = models.CharField(max_length=255 ,null=True)
	amount = models.FloatField()
	account = models.ForeignKey(Account,related_name='transaction' ,on_delete=models.CASCADE)
	trans_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.recipient_name)

