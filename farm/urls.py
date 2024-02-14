from django.urls import path
from .apis import MyFarmDetailAPI, FarmImageUpdateAPI

urlpatterns = [
    path("my", MyFarmDetailAPI.as_view()),
    path("image", FarmImageUpdateAPI.as_view()),
]
