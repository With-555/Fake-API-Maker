from rest_framework import serializers

from apps.backend.models.types import Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = (
            "id",
            "name",
            "type",
            "created_at",
        )
