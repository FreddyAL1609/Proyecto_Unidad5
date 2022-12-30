from . import api
from rest_framework import routers
from django.urls import path
from users.api import LoginView,SignUpView,GetUsers
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register(r'pagos',api.PagosView,'pagos')

pagos_urlpatterns = router.urls

router_user = routers.DefaultRouter()
router_user.register(r'users',GetUsers,basename="read-only")

user_urlpatterns=[
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

user_urlpatterns+=router_user.urls