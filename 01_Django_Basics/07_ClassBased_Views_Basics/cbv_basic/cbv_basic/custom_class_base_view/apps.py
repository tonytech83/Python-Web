from django.apps import AppConfig


class CustomClassBaseViewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cbv_basic.custom_class_base_view'
