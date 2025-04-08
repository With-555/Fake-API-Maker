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
        # Check if the UUID is valid
        if not uuid:
            return Response(
                {"error": "Invalid UUID"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            schema = DynamicSchema.objects.get(uuid=uuid)
        except DynamicSchema.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Dynamic schema not found"
                }, status=status.HTTP_404_NOT_FOUND
            )

        data = {
            "uuid": uuid,
        }

        return Response(data, status=status.HTTP_200_OK)
