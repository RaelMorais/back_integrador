from rest_framework.permissions import BasePermission, SAFE_METHODS

# Permissão personalizada para caso o usuario não seja diretor, poderá realizar apenas métodos get
class IsDirectorOrOnlyRead(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        if request.method in SAFE_METHODS:
            return True 
        return request.user.cargo == 'D'
    
