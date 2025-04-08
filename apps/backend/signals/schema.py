from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.backend.models.schema import DynamicSchema
from apps.backend.tasks.schema import process_schema_task


@receiver(post_save, sender=DynamicSchema)
def cinema_post_save(sender, instance, created, **kwargs):
    if created:
        process_schema_task.delay(instance.id)
