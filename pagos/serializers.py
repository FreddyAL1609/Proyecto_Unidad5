from rest_framework import serializers
from .models import servicios, usuario_pago, pagos_caducados

class serviciosserializers(serializers.ModelSerializer):
    class Meta:
        model = servicios
        fields = ['nombre', 'descripcion', 'logo']

class usuariopagoserializers(serializers.ModelSerializer):
    class Meta:
        model = usuario_pago
        fields = ['id_usuario', 'id_servicio', 'monto', 'fechadepago', 'fechadecaducidad']

class pagoscaducadosserializers(serializers.ModelSerializer):
    class Meta:
        model = pagos_caducados
        fields = ['pago_usuario_id', 'montodemulta']
