from django.core.exceptions import ValidationError
import re


def validate_password(value):
    if len(value) < 8 or len(value) > 20:
        raise ValidationError("Password must be between 8 and 20 characters.")
    if not re.search(r"[A-Z]", value):
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not re.search(r"\d", value):
        raise ValidationError("Password must have at least one number.")
    if not re.search(r"[!@#$%^&*()-_=+{}<>]", value):
        raise ValidationError("Password must have at least one special character.")