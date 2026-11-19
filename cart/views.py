# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem
from products.models import Product

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart_view')

@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(i.total for i in items)
    return render(request, 'cart.html', {'items': items, 'total': total})

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(CartItem, pk=pk, user=request.user)
    item.delete()
    return redirect('cart_view')

@login_required
def update_quantity(request, pk, action):
    item = get_object_or_404(CartItem, pk=pk, user=request.user)
    if action == 'inc':
        item.quantity += 1
    elif action == 'dec' and item.quantity > 1:
        item.quantity -= 1
    item.save()
    return redirect('cart_view')

# Create your views here.
