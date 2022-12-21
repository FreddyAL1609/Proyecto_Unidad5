from django.db import models
from users.models import User
# Create your models here.

class servicios(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    logo = models.CharField(max_length=200)

class usuario_pago(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_servicio = models.ForeignKey(servicios, on_delete=models.CASCADE)
    monto = models.FloatField(default=0.0)
    fechadepago = models.DateField(null=False)
    fechadecaducidad = models.DateField(null=False)

class pagos_caducados(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    pago_usuario_id = models.ForeignKey(usuario_pago, on_delete=models.CASCADE)
    montodemulta = models.CharField(max_length=50)