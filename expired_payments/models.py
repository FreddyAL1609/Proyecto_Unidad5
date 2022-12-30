from django.db import models
from pagos.models import Pago

# Create your models here.
class ExpiredPayment(models.Model):
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    penalty_free_amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.pago
