from rest_framework import serializers
from . import models
        
        

class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OtpCode
        fields = '__all__'