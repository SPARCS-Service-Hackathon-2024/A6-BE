from django.db import models
from common.models import CommonModel


# TODO : 타입에 따른 FK 설정, 검색 태그 설정
class Diary(CommonModel):
    """Diary Model Definition"""

    class TypeChoices(models.TextChoices):
        plant = ("농업일지", "농업일지")
        farm = ("밭자랑", "밭자랑")

    title = models.CharField(max_length=100, help_text="제목")
    description = models.TextField(help_text="본문")
    type = models.CharField(
        max_length=20,
        choices=TypeChoices.choices,
        default=TypeChoices.plant,
        help_text="일지 타입",
    )
    user = models.ForeignKey(
        "users.User",
        related_name="diaries",
        on_delete=models.SET_NULL,
        null=True,
        help_text="작성자",
    )

    def __str__(self):
        return f"{self.title} - {self.user.username}"


class DairyImage(CommonModel):
    """DairyImage Model Definition"""

    diary = models.ForeignKey(
        "diary.Diary", related_name="images", on_delete=models.CASCADE, help_text="일지"
    )
    path = models.TextField(help_text="저장 경로")

    def __str__(self):
        return f"{self.diary.title} - sub image {self.path} ({self.id})"
