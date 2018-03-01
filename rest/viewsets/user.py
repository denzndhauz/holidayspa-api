from rest_framework import viewsets
from rest.serializers import UserSerializer
from rest.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
