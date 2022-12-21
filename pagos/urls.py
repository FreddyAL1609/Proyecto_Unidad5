from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'servicios', api.serviciosviewset, 'servicios')
router.register(r'usuariopago', api.usuariopagoviewset, 'usuariopago')
router.register(r'pagoscaducados', api.pagoscaducadosviewset, 'pagoscaducados')

urlpatterns = router.urls