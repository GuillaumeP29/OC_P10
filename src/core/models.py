from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Permission(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=32, unique=True)
    permissions = models.ManyToManyField(to=Permission)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.title
