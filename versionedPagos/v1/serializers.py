from rest_framework import serializers
from pagos.models import Pago,User

class PagoSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset = User.objects.all(),slug_field='email')
    class Meta:
        model = Pago
        fields = ['id','user','monto','fecha_pago']
        read_only_fields = ['fecha_pago']
    
    def validate_servicio_v1(self,value):
        if value:
            if value.lower() not in ['netflix','amazon video','star+','paramount+']:
                raise serializers.ValidationError('Error, las opciones de servicio son [Netflix,Amazon Video,Star+,Paramount+]')
        return value
