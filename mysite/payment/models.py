from django.db import models
from django.contrib.auth.models import User

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=255)
    routing_number = models.CharField(max_length=255)
    account_holder_name = models.CharField(max_length=255)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
