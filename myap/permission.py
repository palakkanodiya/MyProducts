from rest_framework.permissions import BasePermission

class IsVerified(BasePermission):
    """
    Allows access only to users who are verified (after OTP).
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_verified)
