from django.db import models
from ProjectManager import settings

from core.models import Project, Role

# Create your models here.
class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='member')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    role = models.ForeignKey(Role, related_name='role')

    def __str__(self):
        return f"{self.user} - {self.role} du projet {self.project}"

    class Meta:
        unique_together = ('user', 'project')
