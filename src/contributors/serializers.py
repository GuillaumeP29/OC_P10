from rest_framework.serializers import ModelSerializer
 
from contributors.models import Contributor
 
 
class ContributorListSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project']
 
 
class ContributorDetailSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'role']
