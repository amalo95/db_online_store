from django.shortcuts import render, HttpResponseRedirect, Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from carts.models import Cart
from main_store.models import Order, OrderRelation, Contain, Product
from django.core.urlresolvers import reverse


@login_required
def orders(request):
    inventoryErrorMessage = ""

    current_user = request.user
    user_id = current_user.id
    user_profile = UserProfile.objects.get(user_id=user_id)

    if request.method == 'POST':
        # carts = ""
        print "IN order POST"
        

        cartCollection = Cart.objects.filter(user_id=user_profile.id)
        noInventoryIssue = True;

        #checks to see if its in stock
        for cart in cartCollection:
            product_id = cart.product_id
            invProduct = Product.objects.get(id=product_id)
            if cart.quantity >= invProduct.stock_quantity:
                noInventoryIssue = False;
                inventoryErrorMessage = cart.product.name
                

        if cartCollection and noInventoryIssue:
            newOrder = Order()
            print newOrder.date
            print newOrder.paid
            newOrder.save()
            orderRelation = OrderRelation(order_id=newOrder.id, user_id=user_profile.id)
            orderRelation.save()

            for cart in cartCollection:
                containRelationship= Contain(quantity=cart.quantity, order_id=newOrder.id, product_id=cart.product_id)
                containRelationship.save()
                cart.delete()
        else:
            Cart.objects.all().delete()
            
        orders = OrderRelation.objects.filter(user_id=user_profile.id)
        #return HttpResponseRedirect(reverse('orders'))
    else:
        print "IN order get"
        orders = OrderRelation.objects.filter(user_id=user_profile.id)
        #cart_form = CartForm(data=request.POST)
    return render(request, 'accounts/orders.html', {
        'orders': orders,
        'inventoryErrorMessage': inventoryErrorMessage,
    })

@login_required
def order_detail(request, id):
    try:
        containSet = Contain.objects.filter(order_id=id)
        print "Cart is else"
    except Product.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'accounts/order_detail.html', {
        'containSet': containSet,
    })


@login_required
def edit_account(request):
    if request.method == 'POST':
        
        current_user = request.user
        user_id = current_user.id
        user_profile = UserProfile.objects.get(user_id=user_id)

        user_form = UserForm(data=request.POST, instance=request.user)
        profile_form = UserProfileForm(data=request.POST, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
            'accounts/account_edit.html',
            {'user_form': user_form, 'profile_form': profile_form} )

@login_required
def delete_account(request):
    current_user = request.user
    user_id = current_user.id
    user_profile = UserProfile.objects.get(user_id=user_id)
    if request.method == 'POST':
        current_user.delete()
        user_profile.delete()
        return HttpResponseRedirect(reverse('account'))
    return render(request, 'accounts/account_delete.html', {
        'user_profile': user_profile,
    })

@login_required
def accounts(request):
    current_user = request.user
    user_id = current_user.id
    user_profile = UserProfile.objects.get(user_id=user_id)
    return render(request, 'accounts/account.html', {
        'user_profile': user_profile,
    })

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/login/')


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'registration/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            logged_in = True
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/account/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            logged_in = False
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'registration/login.html', {'logged_in': logged_in})

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        logged_in = True
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'registration/login.html', {'logged_in': logged_in})