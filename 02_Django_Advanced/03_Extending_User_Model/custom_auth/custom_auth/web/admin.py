from django.contrib import admin

from custom_auth.web.models import ModelOne


@admin.register(ModelOne)
class ModelOneAdmin(admin.ModelAdmin):
    pass
