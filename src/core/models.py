from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Permission(models.Model):
    name = models.CharField(max_length=32, unique=True)


class Role(models.Model):
    name = models.CharField(max_length=32, unique=True)
    permissions = models.ManyToManyField(to=Permission)


class ProjectType(models.Model):
    name = models.CharField(max_length=32, unique=True)


class CustomUser(AbstractUser):

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, blank=True)
    type = models.CharField(ProjectType, related_name='project_type')

    def __str__(self):
        return self.title
