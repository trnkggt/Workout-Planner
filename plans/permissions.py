from rest_framework.permissions import BasePermission


class IsOwnerOf(BasePermission):
    """
    Restrict access to users who are not owner of the instance
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsOwnerOfExerciseDetails(BasePermission):
    """
    Restrict access to users who are not owner of the instance
    """
    def has_object_permission(self, request, view, obj):
        return obj.workout_plan.user == request.user
