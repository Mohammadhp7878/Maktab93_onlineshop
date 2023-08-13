from rest_framework import serializers
from . import models
import re


class PhoneSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

    def validate_phone_number(self, phone):
        print(phone)
        phone_pattern = r'(0|\+98)?([ ]|-|[()]){0,2}9[0|1|2|3|4|9]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}'

        if not re.fullmatch(phone_pattern, phone):
            raise serializers.ValidationError("Invalid phone number format")

        return phone