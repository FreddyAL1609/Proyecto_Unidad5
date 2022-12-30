from django.db import models
#BASE MANAGER
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario necesita que is_staff sea verdadero")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario necesita que is_superuser sea verdadero")

        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(unique=True)

    objects=CustomUserManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]

    def __str__(self) -> str:
        return self.email