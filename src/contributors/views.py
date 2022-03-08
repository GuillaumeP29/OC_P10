from rest_framework.viewsets import ReadOnlyModelViewSet
from contributors.serializers import PermissionSerializer, RoleSerializer
from contributors.models import Permission, Role
from core.permissions import IsAdminAuthenticated


class PermissionViewSet(ReadOnlyModelViewSet):
    serializer_class = PermissionSerializer

    permission_classes = [IsAdminAuthenticated, ]

    def get_queryset(self):
        return Permission.objects.all()


class RoleViewSet(ReadOnlyModelViewSet):
    serializer_class = RoleSerializer

    permission_classes = [IsAdminAuthenticated, ]

    def get_queryset(self):
        return Role.objects.all()
