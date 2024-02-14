from rest_framework import serializers
from django.conf import settings
from .models import PlantType


class PlantTypeCreateSerializer(serializers.ModelSerializer):
    main_image = serializers.FileField()

    class Meta:
        model = PlantType
        fields = "__all__"


class PlantTypeReadSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()

    class Meta:
        model = PlantType
        fields = "__all__"

    def get_main_image(self, obj):
        return settings.MEDIA_URL + obj.main_image if obj.main_image else None
