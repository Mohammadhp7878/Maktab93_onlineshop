from rest_framework import serializers
from . import models


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OtpCode
        fields = ["phone_number"]
        
        

class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OtpCode
        fields = ["code"]