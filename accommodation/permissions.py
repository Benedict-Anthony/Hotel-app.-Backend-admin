from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserWriteOnly(BasePermission):
    def has_permission(self, request, view):
        if request in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_agent
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.is_agent:
                return obj.agent == request.user
            return False
        return False