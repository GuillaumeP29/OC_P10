from rest_framework.serializers import ModelSerializer
 
from core.models import CustomUser, Project, Permission, Role, ProjectType
 
 
class UserListSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name']
 
 
class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email']


class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'type']


class ProjectDetailSerializer(ModelSerializer):
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
