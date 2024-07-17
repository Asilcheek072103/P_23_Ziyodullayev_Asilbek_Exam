from django.contrib import admin
from django.contrib.admin import StackedInline
from django.utils.html import format_html

from apps.models import Category, ProductImage, Product, Cart


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = 'slug',


class ProductImageAdmin(StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = ProductImageAdmin,
    exclude = 'slug',

@admin.register(Cart)
class JobAdmin(admin.ModelAdmin):
    pass
