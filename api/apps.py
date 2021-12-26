from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Конфигурация модуля API для магазина"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    verbose_name = 'API'
