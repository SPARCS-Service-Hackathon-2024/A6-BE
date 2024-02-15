from rest_framework import serializers
from .models import Diary, DairyImage, DiaryPlant
from utils.media import save_media
from plant.models import Plant


class PlanetDiaryCreateSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=False, allow_null=True)
    plants = serializers.ListSerializer(
        child=serializers.IntegerField(required=False), required=False
    )
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), write_only=True
    )

    class Meta:
        model = Diary
        fields = ["user", "title", "location", "description", "plants", "image"]

    def create(self, validated_data):
        plants = validated_data.pop("plants", [])
        image = validated_data.pop("image", None)
        validated_data["type"] = "농업일지"
        diary = Diary.objects.create(**validated_data)
        if image:
            file_path, original_name = save_media(image, "diary_plants")
            DairyImage.objects.create(diary=diary, path=file_path)

        if plants:
            for plant in plants:
                diary_plant = DiaryPlant.objects.create(plant_id=plant, diary=diary)
                diary_plant.save()

        return diary


class FarmDiaryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), write_only=True
    )

    class Meta:
        model = Diary
        fields = ["user", "title", "location", "description"]

    def create(self, validated_data):
        user = validated_data.get("user")
        validated_data["farm_image"] = user.farm_image
        plants = Plant.objects.filter(user=user).all()
        validated_data["type"] = "밭자랑"
        diary = Diary.objects.create(**validated_data)
        for plant in plants:
            diary_plant = DiaryPlant.objects.create(plant=plant, diary=diary)
            diary_plant.save()
        return diary
