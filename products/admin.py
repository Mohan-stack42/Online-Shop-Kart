

from django.contrib import admin
from .models import Category, Product, ProductMedia

class ProductMediaInline(admin.TabularInline):
    model = ProductMedia
    extra = 3

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'price', 'stock', 'category', 'created_at']
    list_filter = ['category']
    search_fields = ['product_name']
    inlines = [ProductMediaInline]