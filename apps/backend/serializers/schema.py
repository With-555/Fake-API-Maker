from rest_framework import serializers

from apps.backend.models.schema import DynamicSchema


class DynamicSchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicSchema
        fields = (
            "id",
            "uuid",
            "config",
            "count",
            "expires_in",
            "created_at",
        )
        read_only_fields = (
            "id",
            "uuid",
            "created_at",
        )
