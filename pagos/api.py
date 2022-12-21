from .models import servicios, usuario_pago, pagos_caducados
from .serializers import serviciosserializers, usuariopagoserializers, pagoscaducadosserializers
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, permissions, filters

class serviciosviewset(viewsets.ModelViewSet):
    queryset = servicios.objects.get_queryset().order_by('id')
    serializer_class = serviciosserializers
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]

class usuariopagoviewset(viewsets.ModelViewSet):
    queryset = usuario_pago.objects.get_queryset().order_by('id')
    serializer_class = usuariopagoserializers
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]

class pagoscaducadosviewset(viewsets.ModelViewSet):
    queryset = pagos_caducados.objects.get_queryset().order_by('id')
    serializer_class = pagoscaducadosserializers
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]
