from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Product
from accounts.models import UserProfile
from carts.forms import CartForm
from carts.models import Cart

# Create your views here.



def searchLow(request):
    try:
        q=request.GET.get('q')
    except:
        q=None
        print "holakease"

    if q:   
        query=q
        print query
        print "hello"
        productsLow = Product.objects.filter(name__icontains=q).order_by('price')
        print productsLow
        

    return render(request,'products/search_low.html', {
        'productsLow': productsLow, "query": query,
    })


def searchHigh(request):
    try:
        q=request.GET.get('q')
    except:
        q=None
        print "holakease"

    if q:   
        query=q
        print query
        print "hello"
        productsLow = Product.objects.filter(name__icontains=q).order_by('-price')
        print productsLow
        

    return render(request,'products/search_high.html', {
        'productsLow': productsLow, "query": query,
    })
# def searchLow(request):
#     try:
#         q=request.GET.get('q')
#     except:
#         q=None
#         print "holakease"

#     if q:   
#         query=q
#         print query
#         print "hello"
#         productsLow = Product.objects.filter(name__icontains=q).order_by('price')
#         print productsLow
        

#     return render(request,'products/search_low.html', {
#         'productsLow': productsLow, "query": query,
#     })

def sortLow(request, query):
    try:
        print "inside low: " + query
        productsLow = Product.objects.filter(name__icontains=query).order_by('price')
    except:
        productsLow = None
        print "holakease"
    return render(request,'products/sort_low.html', {
        'productsLow': productsLow, "query": query,
    })

def sortHigh(request, query):
    try:
        print "inside low: " + query
        productsHigh = Product.objects.filter(name__icontains=query).order_by('-price')
    except:
        productsHigh = None
        print "holakease"

    return render(request,'products/sort_high.html', {
        'productsHigh': productsHigh, "query": query,
    })

def index(request):
    products = Product.objects.exclude(stock_quantity=0)
    return render(request, 'products/index.html', {
        'products': products,
    })

def product_detail(request, id):
    print request.method
    print "this ithe id: " + id
    if request.method == 'POST':
        print "Cart is post"
        current_user = request.user

        user_id = current_user.id
        

        user_profile = UserProfile.objects.get(user_id=user_id)
        productInstance = Product.objects.get(id=id)
        
        cartObj = Cart(user=user_profile, product=productInstance)
        cart_form = CartForm(data=request.POST,instance=cartObj)
       
        if cart_form.is_valid():
            print "Cart is valid"
            cart = cart_form.save()


            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            cart.UserProfile_id = user_profile.id
            cart.product_id = id
            print "checking for null" + cart.product_id
            cart.save()

          
            return HttpResponseRedirect(reverse('cart'))
    
    else:
        try:
            product = Product.objects.get(id=id)
            cart_form = CartForm(data=request.POST)
            print "Cart is else"
        except Product.DoesNotExist:
            raise Http404('This item does not exist')
    
    return render(request, 'products/product_detail.html', {
        'product': product,
        'cart_form': cart_form,
    })