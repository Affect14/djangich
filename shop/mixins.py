from django.db import models


class AutoDateMixin(models.Model):
    """Миксин для добавления служебных полей даты создания и обновлени модели."""

    dt_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    dt_updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
    )

    class Meta:
        abstract = True
