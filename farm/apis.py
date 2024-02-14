from rest_framework import generics, status
from rest_framework.response import Response
from plant.models import Plant
from .serializers import MyFarmDetailSerializer
from utils.authentication import IsAuthenticatedCustom


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
