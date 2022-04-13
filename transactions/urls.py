from django.urls import path
from .views import HomeView, TransactionView
from . import views

# app paths
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("account/<int:pk>", TransactionView.as_view(), name="one_account"), 
    path("deposit/<int:pk>", views.deposit_funds, name="deposit_funds"), 
    path('transferfunds/<int:pk>', views.transfer_funds, name="transfer_funds"),
    path('withdrawfunds/<int:pk>', views.withdraw_funds, name="withdraw_funds")
]
