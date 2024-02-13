import jwt, re, os
from datetime import datetime, timedelta
from django.utils import timezone
from django.conf import settings
import random
import string
from .models import User, Jwt
from utils.exceptions import CustomValidationError, CustomAuthorizationError


def get_random(length):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))


def get_access_token(payload):
    exp = timezone.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRATION_TIME)
    return (
        jwt.encode(
            {
                "exp": exp,
                **payload,
            },
            settings.SECRET_KEY,
            algorithm="HS256",
        ),
        exp,
    )


def get_refresh_token():
    exp = timezone.now() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRATION_TIME)
    return (
        jwt.encode(
            {
                "exp": exp,
                "data": get_random(10),
            },
            settings.SECRET_KEY,
            algorithm="HS256",
        ),
        exp,
    )


def decodeJWT(bearer):
    if not bearer:
        return None

    token = bearer[7:]
    try:
        decoded = jwt.decode(token, key=settings.SECRET_KEY, algorithms="HS256")
        exp_datetime = datetime.utcfromtimestamp(decoded["exp"])
        if exp_datetime < timezone.now():
            raise CustomAuthorizationError({"data": "토큰이 만료되었습니다."})
    except jwt.exceptions.ExpiredSignatureError:
        raise CustomAuthorizationError({"data": "토큰이 만료되었습니다."})
    except jwt.exceptions.DecodeError:
        raise CustomAuthorizationError({"data": "올바르지 않은 토큰입니다."})

    if decoded:
        try:
            return User.objects.get(id=decoded["user_id"])
        except User.DoesNotExist:
            return None


def middleware_decodeJWT(bearer):
    if not bearer:
        return None

    token = bearer[7:]
    try:
        decoded = jwt.decode(token, key=settings.SECRET_KEY, algorithms="HS256")
        exp_datetime = datetime.utcfromtimestamp(decoded["exp"])
        if exp_datetime < timezone.now():
            return "TOKEN_EXPIRED"
    except jwt.exceptions.ExpiredSignatureError:
        return "TOKEN_EXPIRED"
    except jwt.exceptions.DecodeError:
        return "TOKEN_INVALID"

    if decoded:
        try:
            return User.objects.get(id=decoded["user_id"])
        except User.DoesNotExist:
            return None
