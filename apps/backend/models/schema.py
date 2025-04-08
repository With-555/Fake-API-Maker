import uuid

from django.db import models

from apps.shared.models.base import AbstractBaseModel


class DynamicSchema(AbstractBaseModel):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, db_index=True
    )
    config = models.JSONField(db_index=True, default=dict)
    count = models.PositiveBigIntegerField(default=0, db_index=True)
    expires_in = models.PositiveIntegerField(default=86400, db_index=True)
    csv = models.FileField(null=True, blank=True, upload_to="dynamic_schemas/csv/")
    json = models.FileField(null=True, blank=True, upload_to="dynamic_schemas/json/")
    xlsx = models.FileField(null=True, blank=True, upload_to="dynamic_schemas/xlsx/")
    is_active = models.BooleanField(default=False, db_index=True)

    class Meta:
        verbose_name = "Dynamic Schema"
        verbose_name_plural = "Dynamic Schemas"
        db_table = "dynamic_schema"
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.uuid)
