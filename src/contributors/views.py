from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from contributors.serializers import ContributorListSerializer, ContributorDetailSerializer
from contributors.models import Contributor

# Create your views here.
class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorListSerializer
    detail_serializer_class = ContributorDetailSerializer

    def get_queryset(self):
        return Contributor.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
