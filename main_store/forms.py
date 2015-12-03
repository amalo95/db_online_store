from django import forms
from .models import Product, Order, OrderRelation, Contain,
from django.contrib.auth.models import User


class CartForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('address',)