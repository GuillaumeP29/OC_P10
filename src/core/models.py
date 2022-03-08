from django.db import models
from django.contrib.auth.models import AbstractUser

from ProjectManager import settings
from contributors.models import Role


class ProjectType(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, blank=True)
    type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(CustomUser, through="Contributor")

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='member')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    role = models.ForeignKey(Role, related_name='role', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user} - {self.role} du projet {self.project}"
