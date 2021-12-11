from rest_framework.serializers import ModelSerializer
 
from contributors.models import Contributor
 
 
class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'role']
