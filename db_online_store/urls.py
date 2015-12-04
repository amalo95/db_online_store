from django.conf.urls import include, url
from django.contrib import admin
from accounts import views as accountsViews
from main_store import views as storeViews

urlpatterns = [
		url(r'^$', storeViews.index, name='index'),
        url(r'^product/(?P<id>\d+)/', storeViews.product_detail, name='product_detail'),
        url(r'^admin/', include(admin.site.urls), name='admin'),
        url(r'^register/$', accountsViews.register, name='register'), # ADD NEW PATTERN!
        url(r'^login/$', accountsViews.user_login, name='login'),
        url(r'^logout/$', accountsViews.user_logout, name='logout'),
        url(r'^account/$', accountsViews.accounts, name='account'),
        url(r'^account/edit/$', accountsViews.edit_account, name='edit_account'),
        url(r'^account/delete/$', accountsViews.delete_account, name='delete_account'),
        url(r'^account/orders/$', accountsViews.orders, name='orders'),
        url(r'^account/cart/$', accountsViews.cart, name='orders'),
]