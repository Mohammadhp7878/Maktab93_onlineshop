from core.models import BaseModel
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser):
    class RoleStatus(models.TextChoices):
        ADMIN = ("A", "admin")
        CUSTOMER = ("C", "customer")

    phone_number = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(
        max_length=1, choices=RoleStatus.choices, default=RoleStatus.CUSTOMER
    )

    USERNAME_FIELD = "phone_number"

    def __str__(self) -> str:
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class UserProfile(models.Model):
    class SexChoice(models.TextChoices):
        MALE = ("M", "male")
        FEMALE = ("F", "female")

    related_user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180)
    email = models.EmailField(unique=True)
    birthday = models.TimeField()
    sex = models.CharField(max_length=1, choices=SexChoice.choices)
    password = models.CharField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Address(BaseModel):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    detail = models.CharField(max_length=255)
    postal_code = models.CharField(unique=True)

    def __str__(self) -> str:
        return f"{self.id}"
