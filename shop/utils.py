import re


def product_image_upload_to(instance, filename: str) -> str:
    """Функия возвращающая путь для сохранения изображения товара"""
    filename = re.sub(r'\s+', '_', filename.lower())
    product_name = re.sub(r'\s+', '_', instance.product.name.lower())

    return f'{instance.product.pk}_{product_name}/{filename}'
