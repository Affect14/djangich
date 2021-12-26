from django.contrib import admin

from shop.models import (
    Category,
    Product,
    ProductImage,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс управления модели категории в панели администратора"""

    list_display = ['name', 'dt_created', 'dt_updated']
    readonly_fields = ['dt_created', 'dt_updated']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс управления модели товара в панели администратора"""

    list_display = ['name', 'category', 'price', 'dt_created', 'dt_updated']
    list_filter = ['category']
    readonly_fields = ['dt_created', 'dt_updated']
    raw_id_fields = ['category']
    search_fields = ['name', 'price']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    """Класс управления модели изображения товара в панели администратора"""

    list_display = ['product', 'id', 'dt_created', 'dt_updated']
    readonly_fields = ['dt_created', 'dt_updated']
    raw_id_fields = ['product']
    search_fields = ['product']
