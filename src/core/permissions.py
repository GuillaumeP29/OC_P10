from rest_framework.permissions import BasePermission
from core.models import Project
from issues.models import Issue, Comment


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class IsContributor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        print(type(obj))
        if (isinstance(obj, Project)):
            project = obj
        elif (isinstance(obj, Issue)):
            project = obj.project
        elif (isinstance(obj, Comment)):
            project = obj.issue.project
        contributors_id_list = []
        for contributor in project.contributors.all():
            contributors_id_list.append(contributor.id)
        if request.user.is_superuser:
            return True
        else:
            return request.user.id in contributors_id_list


class IsAuthorOrOwner(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        else:
            if (isinstance(obj, Project)):
                contributor = obj.contributors.get(project=obj.id, user=request.user)
                return contributor.role.name == 'Owner'
            elif (isinstance(obj, Issue) or isinstance(obj, Comment)):
                return request.user == obj.author
