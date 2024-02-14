from rest_framework import serializers
from django.conf import settings
from .models import PlantType, Plant


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


class PlantCreateSerializer(serializers.ModelSerializer):
    main_image = serializers.FileField(required=False)

    class Meta:
        model = Plant
        fields = "__all__"


class PlantReadSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()
    plant_type = serializers.SerializerMethodField()

    class Meta:
        model = Plant
        fields = "__all__"

    def get_main_image(self, obj):
        return settings.MEDIA_URL + obj.main_image if obj.main_image else None

    def get_plant_type(self, obj):
        plant_type = obj.plant_type
        if plant_type:
            return {"id": plant_type.id, "name": plant_type.name}
        return None
