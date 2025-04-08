import json
import os
from datetime import datetime, timezone
from uuid import UUID

from django.contrib.sites.models import Site
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.schema import DynamicSchema


class DataAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uuid):
        """
        Get data from the server.
        """
        try:
            uuid_obj = UUID(uuid, version=4)
        except ValueError:
            return Response(
                {"success": False, "message": "Invalid UUID format"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            schema = DynamicSchema.objects.get(uuid=uuid_obj)
        except DynamicSchema.DoesNotExist:
            return Response(
                {"success": False, "message": "Dynamic schema not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if not schema.is_active:
            return Response(
                {
                    "success": False,
                    "message": "Please wait while the information is being prepared...",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        created = schema.created_at
        ttl = schema.expires_in
        now = datetime.now(timezone.utc)
        if (now - created).total_seconds() > ttl:
            schema.delete()
            return Response(
                {"success": False, "message": "Expired"}, status=status.HTTP_410_GONE
            )

        data = {}
        json_file_path = schema.json.path if schema.json else None
        if json_file_path and os.path.exists(json_file_path):
            with open(json_file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

        site = Site.objects.get_current()
        domain = f"https://{site.domain}"
        csv_url = f"{domain}{schema.csv.url}" if schema.csv else None
        json_url = f"{domain}{schema.json.url}" if schema.json else None
        xlsx_url = f"{domain}{schema.xlsx.url}" if schema.xlsx else None

        return Response(
            {
                "success": True,
                "message": "Data retrieved successfully",
                "csv": csv_url,
                "json": json_url,
                "schema": xlsx_url,
                "uuid": str(schema.uuid),
                "data": data,
                "created_at": schema.created_at.isoformat(),
                "expires_in": schema.expires_in,
            },
            status=status.HTTP_200_OK,
        )
