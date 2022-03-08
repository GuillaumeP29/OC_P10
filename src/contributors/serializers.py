from rest_framework.serializers import ModelSerializer
 
from contributors.models import Permission, Role
        

class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name']


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'permissions']
