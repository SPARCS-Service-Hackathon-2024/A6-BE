from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import (
    PlantTypeCreateSerializer,
    PlantTypeReadSerializer,
    PlantCreateSerializer,
    PlantReadSerializer,
)
from .models import PlantType, Plant, PlantLog
from django.db import transaction
from utils.media import save_media
from utils.authentication import IsAuthenticatedCustom
from datetime import datetime, timedelta
from .utils import create_plant_log


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


class PlantCreateAPI(generics.CreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantCreateSerializer
    read_serializer = PlantReadSerializer
    permission_classes = (IsAuthenticatedCustom,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        main_image = serializer.validated_data.get("main_image", None)
        plant = serializer.save(user=request.user)
        if main_image:
            file_path, original_name = save_media(main_image, "plants")
            plant.main_image = file_path
            plant.save()
        plant_type = plant.plant_type

        last_watered_at = request.data.get("watered_at")
        last_watered_at = datetime.strptime(last_watered_at, "%Y-%m-%d").date()
        last_repotted_at = request.data.get("repotted_at")
        last_repotted_at = datetime.strptime(last_repotted_at, "%Y-%m-%d").date()

        PlantLog.objects.create(
            plant=plant,
            type="시작",
            deadline=plant.start_at,
            complete_at=plant.start_at,
            is_complete=True,
        )
        watering_log = create_plant_log(
            plant, "물주기", last_watered_at + timedelta(days=plant_type.watering_cycle)
        )
        repot_log = create_plant_log(
            plant, "분갈이", last_repotted_at + timedelta(days=plant_type.repotting_cycle)
        )

        serializer = self.read_serializer(plant)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
