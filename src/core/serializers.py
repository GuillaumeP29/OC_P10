from rest_framework.serializers import ModelSerializer
 
from core.models import CustomUser, Project, Permission, Role, ProjectType
 
 
class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email']


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type']


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name']


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'permissions']


class ProjectTypeSerializer(ModelSerializer):
    class Meta:
        model = ProjectType
        fields = ['id', 'name']
