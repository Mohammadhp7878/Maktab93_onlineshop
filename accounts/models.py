from typing import Iterable, Optional
from core.models import BaseModel
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from utilize import validate_password
from django.core.cache import cache


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.CharField(max_length=6)

    def save(self, *args, **kwargs):
        
        cache.set(self.phone_number, self.code, 120)

    def retrieve_code(self, phone_number):
        if self.phone_number == phone_number:
            return cache.get(self.phone_number)
        
    def __str__(self) -> str:
        return self.phone_number


class User(AbstractBaseUser, PermissionsMixin):
    class RoleStatus(models.TextChoices):
        ADMIN = ("A", "admin")
        CUSTOMER = ("C", "customer")

    phone_number = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(
        max_length=1, choices=RoleStatus.choices, default=RoleStatus.CUSTOMER
    )
    password = models.CharField(validators=[validate_password], null=True)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["password"]

    def __str__(self) -> str:
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    def specify_role(self):
        if self.is_admin:
            self.role = self.RoleStatus.ADMIN


class UserProfile(models.Model):
    class GenderChoice(models.TextChoices):
        MALE = ("M", "male")
        FEMALE = ("F", "female")

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180)
    email = models.EmailField(unique=True)
    birthday = models.TimeField()
    gender = models.CharField(max_length=1, choices=GenderChoice.choices)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Address(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    detail = models.CharField(max_length=255)
    postal_code = models.CharField()

    def __str__(self) -> str:
        return f"{self.id}"


