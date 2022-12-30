from rest_framework import viewsets,permissions,filters,mixins
from pagos.models import Pago
from .serializers import PagoSerializer
from .pagination import PagosPagination

class PagosView(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    pagination_class = PagosPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__id','=fecha_pago','=servicio_v1']
