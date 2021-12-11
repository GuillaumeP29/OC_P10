from django.urls import path
from . import views


urlpatterns = [
    path('', views.project_issues(), name='project_issues'),
    path('<int:id>/', views.edit_issue(), name='edit_issue'),
    path('<int:id>/comments/', views.issue_comments(), name='issue_comments'),
    path('<int:id>/comments/<int:id>/', views.edit_comment(), name='edit_comment'),
]
