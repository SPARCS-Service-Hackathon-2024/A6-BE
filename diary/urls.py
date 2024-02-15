from django.urls import path
from .apis import PlanetDiaryCreateAPI, FarmDiaryCreateAPI

urlpatterns = [
    path("plant", PlanetDiaryCreateAPI.as_view()),
    path("farm", FarmDiaryCreateAPI.as_view()),
]
