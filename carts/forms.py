from django import forms
from accounts.models import UserProfile
from django.contrib.auth.models import User
from carts.models import Cart

class CartForm(forms.ModelForm):
    quantity = forms.IntegerField(initial=1, min_value=1)
    class Meta:
        model = Cart
        fields = ('quantity',)
