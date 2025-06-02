from django.db import models
from django.contrib.auth.models import AbstractUser

funcao = (
    ('D', 'Diretor'),
    ('P', 'Professor')
)

class Usuario(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[],)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    cargo = models.CharField(choices=funcao, max_length=100)
    REQUIRED_FIELDS = ['cargo']

    def __str__(self):
        return self.username
    
status_sensor = [
    ('ativo','ativo'),
    ('inativo', 'inativo')
]
   
class Sensores(models.Model):
    sensor = models.CharField(max_length=255)
    mac_address = models.CharField(max_length=255)
    unidade_medida = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(choices=status_sensor, max_length=55)
    def __str__(self):
        return self.sensor

class Ambientes(models.Model):
    sig = models.PositiveIntegerField(unique=True)
    descricao = models.CharField(max_length=255)
    ni = models.CharField(max_length=255)
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.descricao

class Historico(models.Model):
    sensor = models.ForeignKey(Sensores, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambientes, on_delete=models.CASCADE)
    valor = models.FloatField()
    timestamp = models.DateTimeField() 
    
    def __str__(self):
        return str(self.sensor)
# Create your models here.
