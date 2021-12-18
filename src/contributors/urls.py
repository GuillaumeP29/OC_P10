from django.urls import path
from . import views


urlpatterns = [
    path('', views.ContributorViewSet.as_view({'get': 'list'}), name='project_contributors'),
    path('<int:contributor_id>/', views.ContributorViewSet.as_view({'get': 'list'}), name='delete_contributor'),
]
