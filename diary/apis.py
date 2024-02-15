from rest_framework import generics, status
from rest_framework.response import Response
from .models import Diary, DiaryPlant, DairyImage
from .serializers import PlanetDiaryCreateSerializer


class PlanetDiaryCreateAPI(generics.CreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = PlanetDiaryCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
