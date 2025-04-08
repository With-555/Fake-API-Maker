from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.backend.models.gallery import Gallery


@admin.register(Gallery)
class GalleryAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
    )
    search_fields = ("name",)
