from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and (
                request.user.is_superuser
                or request.user.is_staff
                or request.user.is_admin
            )
        )


class ReadOnlyOrIsAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.method in SAFE_METHODS or request.user.is_admin
        else:
            return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return request.method in SAFE_METHODS or request.user.is_admin
        else:
            return request.method in SAFE_METHODS
