from django.urls import path
from .apis import PlantTypeCreateAPI

urlpatterns = [path("type", PlantTypeCreateAPI.as_view())]
