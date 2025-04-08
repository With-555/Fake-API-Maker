from django.urls import path

from apps.backend.views.data import DataAPIView
from apps.backend.views.schema import DynamicSchemaListView
from apps.backend.views.types import TypeListView

urlpatterns = [
    path("types/", TypeListView.as_view(), name="types"),
    path("generate/", DynamicSchemaListView.as_view(), name="generate"),
    path("data/<str:uuid>/", DataAPIView.as_view(), name="data"),
]
