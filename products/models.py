
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category/", blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products/images/", blank=True, null=True)
    video = models.FileField(upload_to="products/videos/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    @property
    def discount(self):
        if self.old_price and self.old_price > self.price:
            return int((self.old_price - self.price) / self.old_price * 100)
        return 0

class ProductMedia(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="gallery")
    file = models.FileField(upload_to="products/gallery/")

    def __str__(self):
        return f"{self.product.product_name} - {self.file.name}"

    @property
    def is_video(self):
        return self.file.name.lower().endswith(('.mp4', '.mov', '.webm'))