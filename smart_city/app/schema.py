import graphene
from graphene_django.types import DjangoObjectType
from .models import * 


class AmbienteType(DjangoObjectType):
    class Meta: 
        model = Ambientes

class UsuarioType(DjangoObjectType):
    class Meta: 
        model = Usuario

class HistoricoType(DjangoObjectType):
    class Meta: 
        model = Historico

class SensoresType(DjangoObjectType):
    class Meta:
        model = Sensores

class Query(graphene.ObjectType):
    all_ambiente = graphene.List(AmbienteType)
    all_usuario = graphene.List(UsuarioType)
    all_historico = graphene.List(HistoricoType)
    all_sensores = graphene.List(SensoresType)

    def resolve_all_ambiente(root, info):
        return Ambientes.objects.all()
    
    def resolve_all_usuario(root, info):
        return Usuario.objects.all()
    
    def resolve_all_historico(root, info):
        return Historico.objects.all()
    
    def resolve_all_sensores(root, info):
        return Sensores.objects.all()
    
schema = graphene.Schema(query=Query)