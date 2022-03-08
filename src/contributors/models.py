from django.db import models


class Permission(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=32, unique=True)
    permissions = models.ManyToManyField(to=Permission)

    def __str__(self):
        return self.name
