from django.urls import path
from .apis import SignupAPI, LoginAPI, LogoutAPI, RefreshAPI

urlpatterns = [
    path("signup/", SignupAPI.as_view()),
    path("login/", LoginAPI.as_view()),
    path("logout/", LogoutAPI.as_view()),
    path("refresh/", RefreshAPI.as_view()),
]
