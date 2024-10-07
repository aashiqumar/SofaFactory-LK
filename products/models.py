# products/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)  # Allow null or blank

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)  # Allow null or blank
    description = models.TextField()

    def __str__(self):
        return self.name

class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Banner {self.id}"

class PromotionalProduct(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='promotional_products/')
    description = models.TextField()

    def __str__(self):
        return self.name

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
