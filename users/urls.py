from django.urls import include,re_path
from versionedPagos.v1.router import user_urlpatterns as user_v1
from versionedPagos.v2.router import user_urlpatterns as user_v2


urlpatterns=[
    re_path(r'^v1/',include(user_v1),name="usesv1"),
    re_path(r'^v2/',include(user_v2),name="uses"),
]
