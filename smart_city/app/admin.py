from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


admin.site.register(Usuario)
admin.site.register(Historico)
admin.site.register(Ambientes)
admin.site.register(Sensores)
# Register your models here.


class CustomUsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'cargo', 'is_active', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {'fields': ('telefone', 'genero', 'cargo')}),
    )