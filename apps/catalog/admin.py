from django.contrib import admin

from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'price',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
