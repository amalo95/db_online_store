from django.contrib import admin

# Register your models here.
from .models import Product, Order, OrderRelation, Contain, Supply, Supplier
from accounts.models import UserProfile


class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'stock_quantity', 'description','active']


class SupplierAdmin(admin.ModelAdmin):
	list_display = ['name']

class SupplyAdmin(admin.ModelAdmin):

	list_display = ['get_supplier','get_product']
	def get_supplier(self, obj):
		return obj.supplier.name
	def get_product(self, obj):
		return obj.product.name

class OrderAdmin(admin.ModelAdmin):
	list_display = ['get_id', 'date', 'paid']
	def get_id(self, obj):
		return obj.id

class OrderRelationAdmin(admin.ModelAdmin):
	list_display = ['get_order','get_user']
	def get_order(self, obj):
		return obj.order.id
	def get_user(self, obj):
		return obj.user.user.username

class ContainAdmin(admin.ModelAdmin):
	list_display = ['quantity','get_order','get_product']
	def get_order(self, obj):
		return obj.order.id
	def get_product(self, obj):
		return obj.product.name

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderRelation, OrderRelationAdmin)
admin.site.register(Contain, ContainAdmin)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)