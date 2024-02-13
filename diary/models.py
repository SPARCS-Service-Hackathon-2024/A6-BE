from django.db import models
from common.models import CommonModel


# TODO : 타입에 따른 FK 설정, 검색 태그 설정
class Diary(CommonModel):
    """Diary Model Definition"""

    class TypeChoices(models.TextChoices):
        plant = ("농업일지", "농업일지")
        farm = ("밭자랑", "밭자랑")

    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(
        max_length=20, choices=TypeChoices.choices, default=TypeChoices.plant
    )
    user = models.ForeignKey(
        "users.User", related_name="diaries", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"{self.title} - {self.user.username}"


class DairyImage(CommonModel):
    """DairyImage Model Definition"""

    diary = models.ForeignKey(
        "diary.Diary", related_name="images", on_delete=models.CASCADE
    )
    path = models.TextField()

    def __str__(self):
        return f"{self.diary.title} - sub image {self.path} ({self.id})"
