from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.backend.models.schema import DynamicSchema


@admin.register(DynamicSchema)
class DynamicSchemaAdmin(ModelAdmin):
    list_display = (
        "id",
        "uuid",
        "is_active",
        "created_at",
    )
    search_fields = ("uuid",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    readonly_fields = ("uuid", "config")
