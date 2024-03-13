from rest_framework.permissions import BasePermission


class IsAllowedToRetrieve(BasePermission):
    """
    Restrict users who are does not have is_staff=True
    """
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.method == "GET"

    def has_object_permission(self, request, view, obj):
        return True