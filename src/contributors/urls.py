from django.urls import path
from . import views


urlpatterns = [
    path('permissions/', views.PermissionViewSet.as_view({'get': 'list'}), name='permissions'),
    path('roles/', views.RoleViewSet.as_view({'get': 'list'}), name='roles'),
]
