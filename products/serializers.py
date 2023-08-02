from rest_framework import serializers
from . import models


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        fields = "__all__"


class NestedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("name", "slug", "description", "children")


class CategorySerializer(serializers.ModelSerializer):
    children = NestedCategorySerializer(many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = ["name", "slug", "description", "parent", "children"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ["id", "user", "content"]

    def create(self, validated_data):
        product_id = self.context["product_id"]
        if product_id:
            product = models.Product.objects.get(pk=product_id)
            return models.Comment.objects.create(products=product, **validated_data)
        else:
            return models.Comment.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()
    discount_to_price = serializers.FloatField(read_only=True)

    class Meta:
        model = models.Product
        fields = (
            "id",
            "name",
            "categories",
            "slug",
            "description",
            "inventory",
            "price",
            "main_image",
            "max_order",
            "brand",
            "discount_to_price"
        )

    def get_main_image(self, product):
        main_image = product.images
        return GallerySerializer(main_image).data


class BrandSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = models.Brand
        field = "__all__"



class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ["id", "name", "price"]