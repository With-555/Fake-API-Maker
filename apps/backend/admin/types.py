from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.backend.models.types import Type


@admin.register(Type)
class TypeAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
    )
    search_fields = ("name",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
