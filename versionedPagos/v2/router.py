from .api import ServiceViewSet,UsersViewSet, ExpiredPaymentViewSet,PagosViewV2
from rest_framework import routers
from django.urls import path
from users.api import LoginView,SignUpView,GetUsers
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
router_pagos = routers.DefaultRouter()
router_pagos.register(r'pagos',PagosViewV2,'pagosv2')

pagos_urlpatterns = router_pagos.urls

router_service = routers.DefaultRouter()
router_service.register(r"services",ServiceViewSet,basename="service")

services_urlpatterns = router_service.urls

router_expired_payments=routers.DefaultRouter()
router_expired_payments.register(r"expired-payments",ExpiredPaymentViewSet,basename="expired-payment")

expired_payments_urlpatterns = router_expired_payments.urls


router_user=routers.DefaultRouter()
router_user.register(r'users',UsersViewSet,basename="user")
user_urlpatterns=[
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
]


user_urlpatterns += router_user.urls