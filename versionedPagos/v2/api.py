from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated,AllowAny
from services.models import Service
from users.models import User
from expired_payments.models import ExpiredPayment
from .serializers import ServiceSerializer,UserSerializer, ExpiredPaymentSerializer,PagoSerializerV2
from users.serializers import SignUpSerializer
from pagos.models import Pago
from .pagination import PagosPaginationV2
from rest_framework import filters
from .throttle import v2RateThrottle

class PagosViewV2(ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializerV2
    pagination_class = PagosPaginationV2
    filter_backends = [filters.SearchFilter]
    search_fields = ['=fecha_pago','=expiration_date']
    throttle_classes = [v2RateThrottle]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['partial_update','update','destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]     
        return [permission() for permission in permission_classes]
        
    def create(self, request, *args, **kwargs):
        pago = super().create(request, *args, **kwargs)
        ultimo_pago = Pago.objects.order_by('-id').first()
        pago_db = Pago.objects.get(id=ultimo_pago.id)
        if pago_db.expiration_date < pago_db.fecha_pago:
            penalty = pago_db.monto*0.15
            expired_payment = ExpiredPayment(pago=pago_db,penalty_free_amount=penalty)
            expired_payment.save()
        return pago

class ServiceViewSet(ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['destroy','partial_update','update','create']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes=[IsAuthenticated]
        
        return [permission() for permission in permission_classes]


class ExpiredPaymentViewSet(ModelViewSet):

    queryset = ExpiredPayment.objects.all()
    serializer_class = ExpiredPaymentSerializer
    #http_method_names = ['get', 'post', 'head']

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['destroy','partial_update','update']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes=[IsAuthenticated]
        return [permission() for permission in permission_classes]


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_classes = {
        'create': SignUpSerializer,
        
    }
    default_serializer_class = UserSerializer 

    def get_serializer_class(self):
        print(self.action)
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['destroy','partial_update','update','create','retrieve']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes=[IsAuthenticated]
        
        return [permission() for permission in permission_classes]
    