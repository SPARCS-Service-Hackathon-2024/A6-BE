from rest_framework import generics, status
from rest_framework.response import Response
from .models import Diary, DiaryPlant, DairyImage
from .serializers import PlanetDiaryCreateSerializer, FarmDiaryCreateSerializer
from utils.authentication import IsAuthenticatedCustom


class PlanetDiaryCreateAPI(generics.CreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = PlanetDiaryCreateSerializer
    permission_classes = (IsAuthenticatedCustom,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"data": "참 잘했어요!"}, status=status.HTTP_201_CREATED, headers=headers
        )


class FarmDiaryCreateAPI(generics.CreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = FarmDiaryCreateSerializer
    permission_classes = (IsAuthenticatedCustom,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"data": "참 잘했어요!"}, status=status.HTTP_201_CREATED, headers=headers
        )
