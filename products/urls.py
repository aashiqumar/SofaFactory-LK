from django.urls import path
from .views import index, product_list, services, product_detail, blog, blog_detail, blog_category

urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list, name='product_list'),
    path('products/furniture/', product_list, name='furniture'),
    path('services/', services, name='services'),
    path('blog/', blog, name='blog'),
    path('contact/', services, name='contact'),
    path('about/', services, name='about'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('blog/<int:id>/', blog_detail, name='blog_detail'),
    path('blog/category/<int:id>/', blog_category, name='blog_category'),
]