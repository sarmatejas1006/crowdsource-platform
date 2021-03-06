from rest_framework import permissions


class IsProjectOwnerOrCollaborator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class IsReviewerOrRaterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.worker == request.user


class ProjectChangesAllowed(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == 'update' and obj.status != obj.STATUS_DRAFT:
            return False
        return True
