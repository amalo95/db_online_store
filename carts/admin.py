from django.contrib import admin

# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
	list_display = ['get_user','get_product']
	def get_supplier(self, obj):
		return obj.user.username
	def get_product(self, obj):
		return obj.product.name

