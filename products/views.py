# products/views.py
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Product, Banner, PromotionalProduct, Category, BlogPost, BlogCategory
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def index(request):
    products = Product.objects.all()
    banners = Banner.objects.all()
    promotional_products = PromotionalProduct.objects.all()
    return render(request, 'products/index.html', {
        'products': products,
        'banners': banners,
        'promotional_products': promotional_products
    })

def product_list(request):
    categories = Category.objects.all()
    category = request.GET.get('category', 'all')
    if category == 'all':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__name=category)
    return render(request, 'products/furniture.html', {'categories': categories, 'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})

def services(request):
    return render(request, 'products/services.html')

def blog(request):
    posts = BlogPost.objects.all().order_by('-published_date')
    categories = BlogCategory.objects.all()
    return render(request, 'products/blog.html', {'posts': posts, 'categories': categories})


def contact(request):
    return render(request, 'products/contact.html')

def about(request):
    return render(request, 'products/about.html')

def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)  # Fetch the blog post by ID
    return render(request, 'products/blog_detail.html', {'post': post})


def blog_category(request, id):
    category = get_object_or_404(BlogCategory, id=id)
    posts = BlogPost.objects.filter(category=category).order_by('-published_date')
    categories = BlogCategory.objects.all()
    return render(request, 'products/blog.html', {'posts': posts, 'categories': categories})
