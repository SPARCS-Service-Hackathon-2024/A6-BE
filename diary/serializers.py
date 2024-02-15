from rest_framework import serializers
from .models import Diary


class PlanetDiaryCreateSerializer(serializers.ModelSerializer):
    plants = serializers.ListSerializer(
        child=serializers.IntegerField(required=False), required=False
    )
    images = serializers.ListSerializer(
        child=serializers.FileField(required=False), required=False
    )

    class Meta:
        model = Diary
        fields = ["title", "location", "description", "plants", "images"]

    def create(self, validated_data):
        images = validated_data.pop("sub_images", [])
        plants = validated_data.pop("plants", [])
        return super().create(validated_data)
