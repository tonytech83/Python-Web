from rest_framework import permissions

"""
Check if a user is owner
"""


class IsOwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # checks if user and if user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # checks if obj has user equal to `request.user`
        return getattr(obj, 'user', None) == request.user
