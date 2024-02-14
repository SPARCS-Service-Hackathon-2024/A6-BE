from rest_framework import serializers
from plant.models import Plant
from django.conf import settings


class MyFarmDetailSerializer(serializers.ModelSerializer):
    plant_type_name = serializers.SerializerMethodField()
    main_image = serializers.SerializerMethodField()
    last_watered_at = serializers.SerializerMethodField()

    class Meta:
        model = Plant
        fields = [
            "id",
            "nickname",
            "main_image",
            "start_at",
            "plant_type_name",
            "last_watered_at",
        ]

    def get_main_image(self, obj):
        return settings.MEDIA_URL + obj.main_image if obj.main_image else None

    def get_plant_type_name(self, obj):
        if obj.plant_type:
            return obj.plant_type.name
        return None
