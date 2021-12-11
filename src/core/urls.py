from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from . import views


router = routers.SimpleRouter()


urlpatterns = [
    path('', views.LoginPage.as_view(), name='login'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('sign_up/', views.sign_up_page, name='sign_up'),
    path('logout/', views.logout_user, name='logout'),
    path('projects/', views.projects(), name=''),
    path('projects/<int:id>/', views.edit_project()),
    path('projects/<int:id>/users/', include('contributors.urls')),
    path('projects/<int:id>/issues/', include('issues.urls')),
]
