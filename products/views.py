
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    q = request.GET.get('q', '')
    cat_id = request.GET.get('category', '')
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    if q:
        products = products.filter(product_name__icontains=q)
    if cat_id:
        products = products.filter(category_id=cat_id)
    return render(request, 'home.html', {'products': products, 'categories': categories, 'q': q, 'cat_id': cat_id})

def product_detail(request, pk):
    p = get_object_or_404(Product, pk=pk)
    related = Product.objects.filter(category=p.category).exclude(pk=pk)[:4]
    return render(request, 'product_detail.html', {'p': p, 'related': related})