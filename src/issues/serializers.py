from rest_framework.serializers import ModelSerializer
 
from issues.models import Issue, Comment
 
 
class IssueListSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'priority', 'project', 'status']
        
        
class IssueDetailSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            'id', 'title', 'description', 'tag', 'priority', 'project', 'status', 'author', 'assignee', 'created_time'
            ]
        
        
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description', 'author', 'issue']

