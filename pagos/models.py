from django.db import models
from users.models import User
from services.models import Service

# Create your models here.

class Pago(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    monto = models.FloatField(default=0.0)
    fecha_pago = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(null=False)

    def __str__(self):
        return self.monto
