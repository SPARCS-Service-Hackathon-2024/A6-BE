from rest_framework import generics, status
from rest_framework.response import Response
from plant.models import Plant
from .serializers import MyFarmDetailSerializer, FarmImageUpdateSerializer
from utils.authentication import IsAuthenticatedCustom
from utils.media import save_media
from django.conf import settings


class MyFarmDetailAPI(generics.ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = MyFarmDetailSerializer
    permission_classes = (IsAuthenticatedCustom,)

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        return queryset.filter(user=user).all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer_data = self.get_serializer(queryset, many=True).data
        data = {"farm_image": request.user.farm_image, "plants": serializer_data}
        return Response(data)


class FarmImageUpdateAPI(generics.GenericAPIView):
    serializer_class = FarmImageUpdateSerializer
    permission_classes = (IsAuthenticatedCustom,)

    def post(self, request):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        farm_image = serializer.validated_data.get("farm_image", None)
        if farm_image:
            file_path, original_name = save_media(farm_image, "farms")
            user.farm_image = settings.MEDIA_URL + file_path
            user.save()
        return Response({"data": "success"})
