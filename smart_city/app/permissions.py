from rest_framework.permissions import BasePermission

class IsDirector(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.cargo == 'D'
    
class IsDirectorOrProfessor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.cargo == 'P' or request.cargo == 'D'