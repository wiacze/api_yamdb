from rest_framework.permissions import BasePermission, SAFE_METHODS


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
