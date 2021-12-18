from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('', views.LoginPage.as_view(), name='login'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('sign_up/', views.sign_up_page, name='sign_up'),
    path('logout/', views.logout_user, name='logout'),
    path('users/', views.UserViewSet.as_view({'get': 'list'}), name='users_list'),
    path('users/<int:user_id>/', views.UserViewSet.as_view({'get': 'retrieve'}), name='user'),
    path('projects/', views.ProjectViewSet.as_view({'get': 'list'}), name='projects_list'),
    path('projects/<int:project_id>/', views.ProjectViewSet.as_view({'get': 'retrieve'}), name='project'),
    path('projects/<int:project_id>/contributors/', include('contributors.urls')),
    path('projects/<int:project_id>/issues/', include('issues.urls')),
]
