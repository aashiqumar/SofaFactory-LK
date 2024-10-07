from django.contrib import admin
from .models import Category, Product, Banner, PromotionalProduct, BlogPost, BlogCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'price')  # Ensure these fields exist in the Product model

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Banner)
admin.site.register(PromotionalProduct)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'category')
    search_fields = ('title', 'content')
    list_filter = ('category', 'published_date')

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)