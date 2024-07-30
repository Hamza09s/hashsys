from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserSerializer, BuisnessSerializer
from .models import CustomUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=["get"])
    def buisness(self, request, pk=None):
        user = self.get_object()
        buisness = user.buisness
        if buisness:
            serializer = BuisnessSerializer(buisness)
            return Response(serializer.data)
        else:
            return Response(
                {"detail": "This user does not have an associated buisness."},
                status=404,
            )
