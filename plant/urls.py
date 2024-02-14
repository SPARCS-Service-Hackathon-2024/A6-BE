from django.urls import path
from .apis import PlantTypeCreateAPI, PlantCreateAPI, MyPlantLogListAPI

urlpatterns = [
    path("", PlantCreateAPI.as_view()),
    path("type", PlantTypeCreateAPI.as_view()),
    path("log/my", MyPlantLogListAPI.as_view()),
]
