from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if the user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update only their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is tryng to update only their own status"""

        # SAFE_METHODS are create and return, unsafe are update, delet
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
