from rest_framework.permissions import BasePermission

class IsDirector(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.cargo in ['D'] 
        return False
    
class IsDirectorOrProfessor(BasePermission):
    def has_permission(self, request, view):
        # Verifica se o usuário está autenticado e se é 'Diretor' ou 'Professor'
        if request.user.is_authenticated:
            return request.user.cargo in ['D', 'P']  # 'D' para Diretor, 'P' para Professor
        return False