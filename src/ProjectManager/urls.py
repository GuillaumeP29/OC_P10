from django.contrib import admin
from django.urls import path, include
from core.views import UserViewSet, ProjectViewSet, ContributorViewSet
from issues.views import IssueViewSet, CommentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter


router = SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'users', UserViewSet, basename='users')

contributor_router = NestedSimpleRouter(router, r'projects', lookup='project')
contributor_router.register(r'contributors', ContributorViewSet, basename='project-contributors')

issue_router = NestedSimpleRouter(router, r'projects', lookup='project')
issue_router.register(r'issues', IssueViewSet, basename='project-issues')

comment_router = NestedSimpleRouter(issue_router, r'issues', lookup='issue')
comment_router.register(r'comments', CommentViewSet, basename='project-issue-comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/', include(contributor_router.urls)),
    path('api/', include(issue_router.urls)),
    path('api/', include(comment_router.urls)),
    path('api/', include('contributors.urls'))
]
