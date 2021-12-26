from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from api.serializers import ProductSerializer, CategorySerializer
from shop.models import Product, Category


@extend_schema_view(
    get=extend_schema(description='Получить подробный список всех категорий.'),
    post=extend_schema(description='Создать новую категорию.'),
)
class CategoryListAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


@extend_schema_view(
    get=extend_schema(description='Получить подробную информацию о категории.'),
    put=extend_schema(description='Редактировать поля категории.'),
    update=extend_schema(description='Редактировать поля категории.'),
    delete=extend_schema(description='Удалить категорию.'),
)
class CategoryAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


@extend_schema_view(
    get=extend_schema(description='Получить подробный список всех товаров.'),
    post=extend_schema(description='Создать новый товар.'),
)
class ProductListAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


@extend_schema_view(
    get=extend_schema(description='Получить подробную информацию о товаре.'),
    put=extend_schema(description='Редактировать поля товара.'),
    update=extend_schema(description='Редактировать поля товара.'),
    delete=extend_schema(description='Удалить товар.'),
)
class ProductAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
