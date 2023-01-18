from django.contrib.auth import authenticate, login
from django.http import HttpResponseBadRequest
from django.shortcuts import render,redirect
import stripe
from .models import BankAccount, Transaction
from allauth.account.views import LoginView
from .forms import LoginForm

stripe.api_key = "YOUR_STRIPE_SECRET_KEY"
def charge(request, bank_account_id, amount):
    bank_account = BankAccount.objects.get(id=bank_account_id)
    try:
        stripe_charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            source=bank_account.stripe_token,
        )
        transaction = Transaction.objects.create(
            user=request.user,
            bank_account=bank_account,
            amount=amount,
            status=stripe_charge.status
        )
        return render(request, 'confirmation.html', {'transaction': transaction})
    except stripe.error.CardError as e:
        return HttpResponseBadRequest(content=e)

class MyLoginView(LoginView):
    template_name = "payment/login.html"

    
         