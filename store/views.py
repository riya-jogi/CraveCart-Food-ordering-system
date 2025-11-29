from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import FoodItem, Category, Cart, Order, OrderItem

def home_view(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'store/home.html', context)

def about_view(request):
    return render(request, 'store/about.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def add_to_cart(request, food_id):
    food_item = get_object_or_404(FoodItem, id=food_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, food_item=food_item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('home')

@login_required
def increase_cart_item(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required
def decrease_cart_item(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.get_total for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'store/cart.html', context)

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')

@login_required
def checkout_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        return redirect('home')

    total_price = sum(item.get_total for item in cart_items)

    if request.method == 'POST':
        # Combine address fields from the form into a single string
        full_address = f"{request.POST.get('first_name')} {request.POST.get('last_name')}\n"
        full_address += f"{request.POST.get('address')}\n"
        full_address += f"{request.POST.get('city')}, {request.POST.get('pincode')}"
        
        payment_method = request.POST.get('payment_method')

        if full_address and payment_method:
            # Create the order with all the details
            order = Order.objects.create(
                user=request.user, 
                total_price=total_price, 
                shipping_address=full_address,
                payment_method=payment_method
            )
            # Create order items and clear the cart
            for item in cart_items:
                OrderItem.objects.create(order=order, food_item=item.food_item, quantity=item.quantity, price=item.food_item.price)
            cart_items.delete()
            # Redirect to the confirmation page
            return redirect('order_confirmation', order_id=order.id)

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'store/checkout.html', context)

@login_required
def order_confirmation_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/order_confirmation.html', {'order': order})

@login_required
def order_history_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/order_history.html', {'orders': orders})

