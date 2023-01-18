from django.urls import path
from .views import charge, MyLoginView



urlpatterns = [
    path('charge/<int:bank_account_id>/<int:amount>/', charge, name='charge'),
    path('login/',MyLoginView.as_view()),
]
