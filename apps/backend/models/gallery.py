from django.db import models

from apps.shared.models.base import AbstractBaseModel


class Gallery(AbstractBaseModel):
    """
    Gallery model to represent a gallery of images.
    """

    name = models.CharField(
        max_length=255, unique=True, db_index=True, blank=False, null=False
    )
    description = models.TextField(blank=True, null=True)
    images = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
        db_table = "gallery"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
