# sofa_factory/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('products/furniture/', views.product_list, name='furniture'),
    path('product/<int:id>/',  views.product_detail, name='product_detail'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('blog/category/<int:id>/', views.blog_category, name='blog_category'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])