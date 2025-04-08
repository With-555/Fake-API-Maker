from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.serializers.schema import DynamicSchemaSerializer


class DynamicSchemaListView(APIView):
    permission_classes = [AllowAny]
    serializer_class = DynamicSchemaSerializer

    def post(self, request, *args, **kwargs):
        """
        Create a new dynamic schema.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "success": True,
            "message": "Dynamic schema created successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
