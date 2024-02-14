from django.urls import path
from .apis import (
    PlantTypeCreateAPI,
    PlantCreateAPI,
    MyPlantLogListAPI,
    PlantLogCompleteAPI,
    PlantDetailAPI,
)

urlpatterns = [
    path("", PlantCreateAPI.as_view()),
    path("<int:pk>", PlantDetailAPI.as_view()),
    path("type", PlantTypeCreateAPI.as_view()),
    path("log/my", MyPlantLogListAPI.as_view()),
    path("log/complete/<int:pk>", PlantLogCompleteAPI.as_view()),
]
