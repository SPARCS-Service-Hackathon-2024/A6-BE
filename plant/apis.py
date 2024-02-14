from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import PlantTypeCreateSerializer, PlantTypeReadSerializer
from .models import PlantType
from django.db import transaction
from utils.media import save_media


class PlantTypeCreateAPI(generics.ListCreateAPIView):
    queryset = PlantType.objects.all()
    serializer_class = PlantTypeCreateSerializer
    read_serializer = PlantTypeReadSerializer

    def perform_create(self, serializer):
        return serializer.save()

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        main_image = serializer.validated_data.get("main_image", None)
        if main_image:
            file_path, original_name = save_media(main_image, "plant_types")
            instance.main_image = file_path
            instance.save()
        data = self.read_serializer(instance).data
        headers = self.get_success_headers(data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.read_serializer(queryset, many=True)
        return Response(serializer.data)
