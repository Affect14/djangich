from django.core.validators import MinValueValidator
from django.db import models

from shop.mixins import AutoDateMixin
from shop.utils import product_image_upload_to


class Category(AutoDateMixin):
    """Модель категории"""

    name = models.CharField(
        max_length=128,
        verbose_name='Название',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


class Product(AutoDateMixin):
    """Модель товара"""

    name = models.CharField(
        max_length=256,
        verbose_name='Название',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        verbose_name='Категория',
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(0.0)],
        verbose_name='Цена',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return self.name


class ProductImage(AutoDateMixin):
    """Модель изображения товара"""

    image = models.ImageField(
        upload_to=product_image_upload_to,
        verbose_name='Изображение',
    )
    product = models.ForeignKey(
        to='Product',
        on_delete=models.CASCADE,
        verbose_name='Товар',
    )

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'

    def __str__(self) -> str:
        return f'#{self.pk} - {self.product}'
