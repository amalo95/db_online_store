from django.db import models
from accounts.models import UserProfile

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock_quantity = models.IntegerField()
    description = models.TextField()
    active = models.BooleanField()
    def __unicode__(self):
        return u'%s' % (self.name)

class Order(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True)
    paid = models.BooleanField(default=1)
    def __unicode__(self):
        return u'%s' % (self.id)

class OrderRelation(models.Model):
    order = models.ForeignKey('Order')
    user = models.ForeignKey('accounts.UserProfile')

class Contain(models.Model):
    quantity = models.IntegerField()
    order = models.ForeignKey('Order')
    product = models.ForeignKey('Product')
    def __unicode__(self):
        return u'id: %s %s qty: %s' % (self.id, self.product.name, self.quantity)

class Supplier(models.Model):
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return u'%s' % (self.name)

class Supply(models.Model):
	supplier = models.ForeignKey('Supplier')
	product = models.ForeignKey('Product')