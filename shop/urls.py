from django.urls import path

from shop.views import (
    categories_list,
    category_detail,
    products_list,
    product_detail,
)

urlpatterns = [
    path('categories/', categories_list, name='categories_list'),
    path('categories/<int:category_id>', category_detail, name='category_detail'),
    path('products/', products_list, name='products_list'),
    path('products/<int:product_id>', product_detail, name='product_detail'),
]
