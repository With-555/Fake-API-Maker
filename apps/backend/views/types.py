from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.types import Type
from apps.backend.serializers.types import TypeSerializer


class TypeListView(APIView):
    permission_classes = [AllowAny]
    serializer_class = TypeSerializer

    def get_queryset(self):
        """
        Returns the queryset of all types.
        """
        return Type.objects.filter(is_active=True)

    def get(self, request):
        types = self.get_queryset()
        serializer = self.serializer_class(types, many=True)
        return Response(
            {
                "success": True,
                "message": "Types retrieved successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
