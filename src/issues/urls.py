from django.urls import path
from . import views


urlpatterns = [
    path('', views.IssueViewSet.as_view({'get': 'list'}), name='issues_list'),
    path('<int:issue_id>/', views.IssueViewSet.as_view({'get': 'retrieve'}), name='issue'),
    path('<int:issue_id>/comments/', views.CommentViewSet.as_view({'get': 'list'}), name='comments_list'),
    path(
        '<int:issue_id>/comments/<int:comment_id>/',
        views.CommentViewSet.as_view({'get': 'retrieve'}),
        name='comment'
        ),
]
