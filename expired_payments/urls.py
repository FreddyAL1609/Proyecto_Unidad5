from django.urls import re_path,include
from versionedPagos.v2.router import expired_payments_urlpatterns as expired_payments_v2


urlpatterns = [
    re_path(r'^v2/',include(expired_payments_v2),name="expired_pay"),
]
