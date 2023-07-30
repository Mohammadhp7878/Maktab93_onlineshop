from rest_framework import serializers
from . import models


class NestedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("name", "slug", "description", "children")


class CategorySerializer(serializers.ModelSerializer):
    children = NestedCategorySerializer(many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = ["name",  "slug", "description", "parent", "children"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ["name", "description", "price", "images"]


class BrandSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = models.Brand
        field = "__all__"
