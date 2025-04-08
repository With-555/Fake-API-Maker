from django.db import models

from apps.shared.models.base import AbstractBaseModel


class FieldType(models.TextChoices):
    CharField = "CharField", "CharField"
    TextField = "TextField", "TextField"
    IntegerField = "IntegerField", "IntegerField"
    FloatField = "FloatField", "FloatField"
    BooleanField = "BooleanField", "BooleanField"
    DateField = "DateField", "DateField"
    DateTimeField = "DateTimeField", "DateTimeField"
    TimeField = "TimeField", "TimeField"
    EmailField = "EmailField", "EmailField"
    URLField = "URLField", "URLField"
    SlugField = "SlugField", "SlugField"
    UUIDField = "UUIDField", "UUIDField"
    ImageField = "ImageField", "ImageField"
    FileField = "FileField", "FileField"
    DecimalField = "DecimalField", "DecimalField"
    IPAddressField = "IPAddressField", "IPAddressField"
    GenericIPAddressField = "GenericIPAddressField", "GenericIPAddressField"
    PhoneNumberField = "PhoneNumberField", "PhoneNumberField"
    BinaryField = "BinaryField", "BinaryField"
    DurationField = "DurationField", "DurationField"
    JSONField = "JSONField", "JSONField"
    SmallIntegerField = "SmallIntegerField", "SmallIntegerField"
    PositiveIntegerField = "PositiveIntegerField", "PositiveIntegerField"
    PositiveSmallIntegerField = "PositiveSmallIntegerField", "PositiveSmallIntegerField"
    BigIntegerField = "BigIntegerField", "BigIntegerField"


class Type(AbstractBaseModel):
    """
    Type model to represent a type of item in the system.
    """

    name = models.CharField(max_length=255, unique=True, db_index=True)
    type = models.CharField(
        max_length=255, db_index=True, choices=FieldType, default=FieldType.CharField
    )
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"
        db_table = "type"
        ordering = ["name"]

    def __str__(self):
        return self.name
