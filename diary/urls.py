from django.urls import path
from .apis import PlanetDiaryCreateAPI

urlpatterns = [path("plant", PlanetDiaryCreateAPI.as_view())]
