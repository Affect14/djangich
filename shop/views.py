from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from shop.models import Category, Product


@require_GET
def categories_list(request: HttpRequest) -> HttpResponse:
    """View: Список категорий"""
    categories = Category.objects.all()

    return render(
        request=request,
        template_name='categories_list.html',
        context={
            'categories': categories,
        },
    )


@require_GET
def category_detail(request: HttpRequest, category_id: int) -> HttpResponse:
    """View: Категория"""
    category = get_object_or_404(Category, pk=category_id)

    return render(
        request=request,
        template_name='category.html',
        context={
            'category': category,
        },
    )


@require_GET
def products_list(request: HttpRequest) -> HttpResponse:
    """View: Список товаров"""
    products = Product.objects.all()

    return render(
        request=request,
        template_name='products_list.html',
        context={
            'products': products,
        },
    )


@require_GET
def product_detail(request: HttpRequest, product_id: int) -> HttpResponse:
    """View: Категория"""
    product = get_object_or_404(Product, pk=product_id)

    return render(
        request=request,
        template_name='product.html',
        context={
            'product': product,
        },
    )
