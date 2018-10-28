from rest_framework import permissions

class OnlySuperUser(permissions.BasePermission):
    message = 'You not allowed.'

    def has_permission(self, request, view):
        
        return request.user.is_superuser
