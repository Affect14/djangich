from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from api.views import (
    CategoryListAPIView,
    CategoryAPIView,
    ProductListAPIView,
    ProductAPIView,
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name='category'),

    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
]
