from services.models import Service
from rest_framework import serializers
from expired_payments.models import ExpiredPayment
from users.models import User
from pagos.models import Pago

class PagoSerializerV2(serializers.ModelSerializer):
    user=serializers.SlugRelatedField(queryset=User.objects.all(),slug_field="email")
    class Meta:
            model = Pago
            fields = ['id','user','service','monto','fecha_pago','expiration_date']
            read_only_fields = ['fecha_pago']


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'

class ExpiredPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpiredPayment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        read_only=("password",)