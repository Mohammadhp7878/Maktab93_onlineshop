from typing import Optional
from django.db import models
from django.contrib.auth.models import _AnyUser, AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    class RoleStatus(models.TextChoices):
        ADMIN = ('A', 'admin')
        CUSTOMER = ('C', 'customer')
    phone_number = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(max_length=1, choices=RoleStatus.choices, default=RoleStatus.CUSTOMER)

    USERNAME_FIELD = 'phone_number'
    
    def has_perm(self, perm, obj=None) :
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    

class UserProfile(models.Model):
    class SexChoice(models.TextChoices):
        MALE = ('M', 'male')
        FEMALE = ('F', 'female')
    user = models.OneToOneField(to=User)
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180)
    email = models.EmailField(unique=True)
    birthday = models.TimeField()
    sex = models.CharField(max_length=1, choices=SexChoice.choices)
    password = models.CharField()