from rest_framework import permissions


class GameAdminPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsNotAuthenticatedPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return not request.user.is_authenticated


class OwnerPermission(permissions.BasePermission):
    def __init__(self, owner_field_name='owner'):
        self.owner_field_name = owner_field_name

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return getattr(obj, self.owner_field_name) == request.user