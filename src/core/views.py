from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models import CustomUser, Project, ProjectType, Contributor
from core.permissions import IsContributor, IsAuthorOrOwner, IsAdminAuthenticated
from core.serializers import (
    UserListSerializer, UserDetailSerializer, ProjectDetailSerializer,
    ProjectListSerializer, ProjectTypeSerializer, ContributorSerializer)  # RegisterUserSerializer,


class UserViewSet(ModelViewSet):
    serializer_class = UserDetailSerializer

    list_serializer_class = UserListSerializer

    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return CustomUser.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return self.list_serializer_class
        return super().get_serializer_class()


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer

    permission_classes = [IsAuthorOrOwner, ]

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs['project_pk'])

    def get_serializer_class(self):
        return self.serializer_class


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectDetailSerializer
    list_serializer_class = ProjectListSerializer

    def get_permissions(self):
        if self.action == ('update' or 'destroy'):
            self.permission_classes = [IsAuthorOrOwner, ]
        else:
            self.permission_classes = [IsContributor, ]
        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        queryset = Project.objects.all()
        if user.is_superuser:
            return queryset
        else:
            user_contributions = Contributor.objects.filter(user=user.id)
            user_contributions_id_list = []
            for contribution in user_contributions:
                user_contributions_id_list.append(contribution.project.id)
            print(user_contributions_id_list)
            queryset = queryset.filter(id__in=user_contributions_id_list)
            return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return self.list_serializer_class
        return super().get_serializer_class()


class ProjectTypeViewSet(ReadOnlyModelViewSet):
    serializer_class = ProjectTypeSerializer

    permission_classes = [IsAdminAuthenticated, ]

    def get_queryset(self):
        return ProjectType.objects.all()
