from django.db import models
from core.models import CustomUser, Project

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_lenght= 1024)
    tag = models.CharField()
    priority = models.CharField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField
    author_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assignee_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_time = models.DateTimeField


class Comment(models.Model):
    description = models.CharField(max_length=1024)
    author_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
