from django.db import models
from common.models import CommonModel


class PlantType(CommonModel):
    """Plant Model Definition"""

    name = models.CharField(max_length=50)
    main_image = models.TextField(blank=True, null=True, default="")
    watering_cycle = models.PositiveIntegerField()
    repotting_cycle = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Plant(CommonModel):
    """PersonalPlant Model Definition"""

    nickname = models.CharField(max_length=50)
    main_image = models.TextField(blank=True, null=True, default="")
    plant_type = models.ForeignKey(
        "plant.PlantType",
        related_name="plants",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    start_at = models.DateField()
    user = models.ForeignKey(
        "users.User",
        related_name="plants",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.user.username}의 {self.nickname}({self.plant_type.name})"


class PlantLog(CommonModel):
    """PlantLog Model Definition"""

    class TypeChoices(models.TextChoices):
        watering = ("물주기", "물주기")
        start = ("시작", "시작")
        repotting = ("분갈이", "분갈이")

    type = models.CharField(
        max_length=20, choices=TypeChoices.choices, default=TypeChoices.watering
    )
    deadline = models.DateField(null=True, blank=True)
    complete_at = models.DateField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    plant = models.ForeignKey(
        "plant.Plant", related_name="logs", on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            f"{self.plant.nickname} {self.type} - {'완료' if self.is_complete else '미완료'}"
        )
