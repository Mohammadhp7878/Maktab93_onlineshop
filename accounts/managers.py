from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(phone_number):
        ...