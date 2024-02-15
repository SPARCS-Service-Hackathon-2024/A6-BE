from django.urls import path
from .apis import PlanetDiaryCreateAPI, FarmDiaryCreateAPI, DiaryListAPI

urlpatterns = [
    path("", DiaryListAPI.as_view()),
    path("plant", PlanetDiaryCreateAPI.as_view()),
    path("farm", FarmDiaryCreateAPI.as_view()),
]
