"""
URL configuration for the core app
Defines URL patterns for the home view
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop_view, name="shop"),
    path("card-detail/<int:id>", views.card_view, name="card-detail"),
    path("create-checkout-session/<int:id>", views.create_checkout, name="create-checkout-session"),
    path("success/", views.payment_success, name="payment-success"),
    path("cancel/", views.payment_cancel, name="payment-cancel"),
]
