from django.urls import path
from . import views


urlpatterns = [
    path('', views.project_contributors(), name='project_contributors'),
    path('<int:id>/', views.delete_contributor(), name='delete_contributor'),
]
