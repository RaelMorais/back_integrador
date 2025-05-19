from rest_framework.permissions import BasePermission

class IsDirector(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.cargo == 'D'
    
class IsDirectorOrProfessor(BasePermission):
    """
    Permissão para permitir acesso apenas a Diretores ou Professores.
    """
    def has_permission(self, request, view):
        # Verifica se o usuário está autenticado e se é 'Diretor' ou 'Professor'
        if request.user.is_authenticated:
            return request.user.cargo in ['D', 'P']  # 'D' para Diretor, 'P' para Professor
        return False