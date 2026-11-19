# orders/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order, OrderItem

@login_required
def checkout(request):
    items = CartItem.objects.filter(user=request.user)
    if not items.exists():
        return redirect('home')
    total = sum(i.total for i in items)
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_amount=total,
            name=request.POST.get('name'),
            address=request.POST.get('address'),
            phone=request.POST.get('phone')
        )
        for i in items:
            OrderItem.objects.create(order=order, product=i.product, quantity=i.quantity, price=i.product.price)
            # Reduce stock
            i.product.stock -= i.quantity
            i.product.save()
        items.delete()
        return redirect('bill', pk=order.id)
    return render(request, 'checkout.html', {'items': items, 'total': total})

@login_required
def bill(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'bill.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bill.html', {'my_orders': orders, 'is_list': True})
# Create your views here.
