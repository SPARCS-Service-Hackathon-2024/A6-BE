from django.db import models
from common.models import CommonModel
from django.utils import timezone


class PlantType(CommonModel):
    """Plant Model Definition"""

    name = models.CharField(max_length=50, help_text="이름")
    main_image = models.TextField(blank=True, null=True, default="", help_text="대표 이미지")
    watering_cycle = models.PositiveIntegerField(help_text="물주기 주기")
    repotting_cycle = models.PositiveIntegerField(help_text="분갈이 주기")

    def __str__(self):
        return f"{self.id} {self.name}"


class Plant(CommonModel):
    """PersonalPlant Model Definition"""

    nickname = models.CharField(max_length=50, help_text="별명")
    main_image = models.TextField(blank=True, null=True, default="", help_text="대표 이미지")
    plant_type = models.ForeignKey(
        "plant.PlantType",
        related_name="plants",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="식물 종류",
    )
    start_at = models.DateField(help_text="시작일")
    user = models.ForeignKey(
        "users.User",
        related_name="plants",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="유저",
    )

    def __str__(self):
        return f"{self.user.username}의 {self.nickname}"


class PlantLog(CommonModel):
    """PlantLog Model Definition"""

    class TypeChoices(models.TextChoices):
        watering = ("물주기", "물주기")
        start = ("시작", "시작")
        repotting = ("분갈이", "분갈이")

    type = models.CharField(
        max_length=20,
        choices=TypeChoices.choices,
        default=TypeChoices.watering,
        help_text="로그 타입",
    )
    deadline = models.DateField(null=True, blank=True, help_text="마감일")
    complete_at = models.DateField(null=True, blank=True, help_text="완료일")
    is_complete = models.BooleanField(default=False, help_text="완료 여부")
    plant = models.ForeignKey(
        "plant.Plant", related_name="logs", on_delete=models.CASCADE, help_text="식물"
    )

    def save(self, *args, **kwargs):
        if self.is_complete and not self.complete_at:
            self.complete_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.plant.nickname} {self.type} - {'완료' if self.is_complete else '미완료'}"
        )
