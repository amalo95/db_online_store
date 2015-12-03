"""db_online_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
1. Add an import:  from my_app import views
2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
1. Add an import:  from other_app.views import Home
2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
1. Add an import:  from blog import urls as blog_urls
2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))


#url('^', include('django.contrib.auth.urls')),

	url(r'^register/$', accountsViews.register, name='register'),
	url(r'^login/$', accountsViews.user_login, name='login'),
"""
from django.conf.urls import include, url
from django.contrib import admin
from main_store import views as storeViews
from accounts import views as accountsViews
#from django.views.generic.edit import CreateView

urlpatterns = [
	url(r'^$', storeViews.index, name='index'),
	url(r'^product/(?P<id>\d+)/', storeViews.product_detail, name='product_detail'),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', accountsViews.register, name='register'), # ADD NEW PATTERN!
    url(r'^login/$', accountsViews.user_login, name='login'),
    url(r'^logout/$', accountsViews.user_logout, name='logout'),
]
