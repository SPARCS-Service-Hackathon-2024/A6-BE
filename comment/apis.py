from rest_framework import generics
from .models import Comment
from .serializers import CommentCreateSerializer
from utils.authentication import IsAuthenticatedCustom


class CommentCreateAPI(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticatedCustom,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
