from django.db import models
from accounts.models import UserProfile

class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	stock_quantity = models.IntegerField()
	description = models.TextField()
	active = models.BooleanField()

class Order(models.Model):
	date = models.DateField(auto_now=True, auto_now_add=False)
	paid = models.BooleanField()

class OrderRelation(models.Model):
	order = models.ForeignKey('Order')
	user = models.ForeignKey('accounts.UserProfile')

class Contain(models.Model):
	quantity = models.IntegerField()
	order = models.ForeignKey('Order')
	product = models.ForeignKey('Product')

class Supplier(models.Model):
	name = models.CharField(max_length=100)

class Supply(models.Model):
	supplier = models.ForeignKey('Supplier')
	product = models.ForeignKey('Product')