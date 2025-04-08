from django.db import models

from apps.shared.models.base import AbstractBaseModel


class Type(AbstractBaseModel):
    """
    Type model to represent a type of item in the system.
    """
    name = models.CharField(max_length=255, unique=True, db_index=True)
    type = models.CharField(max_length=255, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"
        db_table = "type"
        ordering = ["name"]

    def __str__(self):
        return self.name
