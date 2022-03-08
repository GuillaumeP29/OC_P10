from rest_framework.viewsets import ModelViewSet
from issues.serializers import IssueListSerializer, IssueDetailSerializer, CommentSerializer
from issues.models import Issue, Comment
from core.permissions import IsAuthorOrOwner, IsContributor


class IssueViewSet(ModelViewSet):
    queryset = Issue.objects.all()

    serializer_class = IssueDetailSerializer
    list_serializer_class = IssueListSerializer

    def get_permissions(self):
        if self.action == ('update' or 'destroy'):
            self.permission_classes = [IsAuthorOrOwner, ]
        else:
            self.permission_classes = [IsContributor, ]
        return super().get_permissions()

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])

    def get_serializer_class(self):
        if self.action == 'list':
            return self.list_serializer_class
        return super().get_serializer_class()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == ('update' or 'destroy'):
            self.permission_classes = [IsAuthorOrOwner, ]
        else:
            self.permission_classes = [IsContributor, ]
        return super().get_permissions()

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])
