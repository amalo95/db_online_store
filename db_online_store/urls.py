from django.conf.urls import include, url
from django.contrib import admin
from accounts import views as accountsViews
from main_store import views as storeViews
from carts import views as cartViews

# url(r'^lowtohigh/q', accountsViews.order_detail, name='order_detail'),
#         url(r'^hightolow/q', accountsViews.order_detail, name='order_detail'),
#         url(r'^s/[.*]q=(?P<low_high>.*)',views.sortLow, name='sortLow'),
#         url(r'^s/',views.search, name='search'),

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
        url(r'^account/cart/$', cartViews.cart, name='cart'),
        url(r'^account/orders/$', accountsViews.orders, name='orders'),
        url(r'^account/orders/(?P<id>\d+)/', accountsViews.order_detail, name='order_detail'),
        url(r'^low/q=(?P<query>.*)', storeViews.sortLow, name='sortLow'),
        url(r'^high/q=(?P<query>.*)', storeViews.sortHigh, name='sortHigh'),
        url(r'^search/low/', storeViews.searchLow, name='searchLow'),
        url(r'^search/high/', storeViews.searchHigh, name='searchHigh'),
        
        
]