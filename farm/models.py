from django.db import models
from common.models import CommonModel


class Farm(CommonModel):
    """Farm Model Definition"""

    user = models.ForeignKey(
        "users.User",
        related_name="farm",
        on_delete=models.SET_NULL,
        null=True,
        help_text="유저",
    )
    image = models.TextField(blank=True, null=True, default="", help_text="밭 이미지")

    def __str__(self):
        return f"{self.user.username}의 밭"


# TODO : lat, lon, plant
# class FarmButton(CommonModel):
#     """FarmButton Model Definition"""
