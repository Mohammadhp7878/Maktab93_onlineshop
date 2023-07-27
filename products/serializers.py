from rest_framework import serializers
from . import models


class Comment(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name', 'description', 'parent']