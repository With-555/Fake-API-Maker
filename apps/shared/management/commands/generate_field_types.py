from django.core.management.base import BaseCommand

from apps.backend.models.types import FieldType, Type


class Command(BaseCommand):
    help = "Generate Type entries for all FieldType choices"

    def handle(self, *args, **kwargs):
        created_count = 0
        for field_type in FieldType.choices:
            name = field_type[1]
            type_value = field_type[0]

            obj, created = Type.objects.get_or_create(
                name=name,
                defaults={"type": type_value, "is_active": True}
            )

            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"Created: {name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Already exists: {name}"))

        self.stdout.write(self.style.SUCCESS(f"\nDone. {created_count} new types created."))
