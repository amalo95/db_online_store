from django.contrib import admin

from .models import Cart
# Register your models here.
class CartsAdmin(admin.ModelAdmin):
	list_display = ['get_user','get_product','quantity']
	def get_user(self, obj):
		return obj.user.user
	def get_product(self, obj):
		return obj.product.name

admin.site.register(Cart, CartsAdmin)

