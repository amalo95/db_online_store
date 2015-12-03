from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Product

# Create your views here.
def index(request):
	products = Product.objects.exclude(stock_quantity=0)
	return render(request, 'products/index.html', {
		'products': products,
	})

def product_detail(request, id):
	try:
		product = Product.objects.get(id=id)
		current_user = request.user
	    user_id = current_user.id
	    user_profile = UserProfile.objects.get(user_id=user_id)
	    if request.method == 'POST':
	        current_user.delete()
	        user_profile.delete()
	        return HttpResponseRedirect(reverse('account'))
	except Product.DoesNotExist:
		raise Http404('This item does not exist')

    return render(request, 'products/product_detail.html', {
		'product': product,
	})