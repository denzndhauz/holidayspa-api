from dry_rest_permissions.generics import DRYPermissions
from rest_framework import viewsets
from rest.serializers import UserSerializer
from rest.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (DRYPermissions,)
    serializer_class = UserSerializer
