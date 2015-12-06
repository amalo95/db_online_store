from django.db import models
from django.conf import settings
from accounts.models import UserProfile
from main_store.models import Product
# Create your models here.

class Cart(models.Model):
	user = models.ForeignKey('accounts.UserProfile')
	product = models.ForeignKey('main_store.Product')
	quantity = models.PositiveIntegerField(default=1)
	product_price = models.DecimalField(decimal_places=2,max_digits=10)
	agg_price = models.DecimalField(decimal_places=2,max_digits=10)