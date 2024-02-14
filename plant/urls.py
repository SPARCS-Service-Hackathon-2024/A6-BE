from django.urls import path
from .apis import PlantTypeCreateAPI, PlantCreateAPI

urlpatterns = [
    path("type", PlantTypeCreateAPI.as_view()),
    path("", PlantCreateAPI.as_view()),
]
