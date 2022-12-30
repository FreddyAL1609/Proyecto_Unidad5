from django.urls import re_path,include
from versionedPagos.v2.router import services_urlpatterns as services_v2


urlpatterns = [
    re_path(r'^v2/',include(services_v2),name="servic"),
]

