from django.shortcuts import render, HttpResponseRedirect, Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Sum, F

from accounts.forms import UserForm, UserProfileForm
from accounts.models import UserProfile
from .models import Cart

# Create your views here.
@login_required
def cart(request):
    if request.method == 'POST':
        carts = ""
        print "IN CART POST"
        # current_user = request.user
        # user_id = current_user.id
        # user_profile = UserProfile.objects.get(user_id=user_id)

        # cart_form = CartForm(data=request.POST)
       
        # if cart_form.is_valid():
        #     cart = cart_form.save()


        #     # Now we hash the password with the set_password method.
        #     # Once hashed, we can update the user object.
        #     cart.UserProfile_id = user_profile.id
        #     cart.product_id = request.product.id
        #     cart.save()

          
        #     return HttpResponseRedirect(reverse('index'))
    else:
    	print "IN CART get"
    	current_user = request.user
    	user_id = current_user.id
    	user_profile = UserProfile.objects.get(user_id=user_id)
    	user_profile_id = user_profile.id
    	print user_profile_id
    	carts = Cart.objects.filter(user_id=user_profile_id)

        total = carts.aggregate(total=Sum(F('quantity')))
        #cart_form = CartForm(data=request.POST)
    return render(request,
            'accounts/cart.html',
            {'carts': carts,
            'total': total,} )

# def index(request):
#     products = Product.objects.exclude(stock_quantity=0)
#     return render(request, 'products/index.html', {
#         'products': products,
#     })