from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from issues.serializers import IssueListSerializer, IssueDetailSerializer, CommentSerializer
from issues.models import Issue, Comment

# Create your views here.
class IssueViewSet(ModelViewSet):
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer

    def get_queryset(self):
        return Issue.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
