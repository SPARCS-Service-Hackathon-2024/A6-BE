from django.urls import path
from .apis import MyFarmDetailAPI, FarmImageUpdateAPI, UserFarmListAPI

urlpatterns = [
    path("my", MyFarmDetailAPI.as_view()),
    path("image", FarmImageUpdateAPI.as_view()),
    path("target", UserFarmListAPI.as_view()),
]
