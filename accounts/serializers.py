from rest_framework import serializers
from . import models


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OtpCode
        fields = ["phone_number"]


class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OtpCode
        fields = "__all__"
