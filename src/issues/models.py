from django.db import models
from core.models import CustomUser, Project
from ProjectManager.settings import AUTH_USER_MODEL

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    tag = models.CharField(max_length=32)
    priority = models.CharField(max_length=32)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=32)
    author = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    assignee = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignee')
    created_time = models.DateTimeField

    def __str__(self):
        return f"{self.project} - {self.title}"


class Comment(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.issue} - {self.pk}"
