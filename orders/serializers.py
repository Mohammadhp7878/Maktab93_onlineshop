from rest_framework import serializers
from products.serializers import SimpleProductSerializer
from . import models


class CartProductSerializer(serializers.ModelSerializer):
    products = SimpleProductSerializer()
    item_total_price = serializers.SerializerMethodField()

    class Meta:
        model = models.CartProduct
        fields = ["id", "products", "quantity", "item_total_price"]

    def get_item_total_price(self, cart_products: models.CartProduct):
        if cart_products.products.discount:
            return cart_products.quantity * cart_products.products.discount_to_price
        return cart_products.quantity * cart_products.products.price


class CartSerializer(serializers.ModelSerializer):
    cartproducts = CartProductSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = models.Cart
        fields = ["id", "cartproducts", "total_price"]

    def get_total_price(self, cart: models.Cart):
        return sum(
            [
                item.quantity * item.products.price
                if not item.products.discount
                else item.quantity * item.products.discount_to_price
                for item in cart.cartproducts.all()
            ]
        )


class AddProductSerializer(serializers.ModelSerializer):
    products_id = serializers.IntegerField()

    class Meta:
        model = models.CartProduct
        fields = ["id", "quantity", "products_id"]
        
    def validate_products_id(self, value):
        if models.Product.objects.filter(id=value).exists():
            return value
        raise serializers.ValidationError('product does not exists')
    
    
    def save(self, **kwargs):
        carts_id = int(self.context["cart_id"])
        products_id = int(self.validated_data["products_id"])
        quantity = self.validated_data["quantity"]

        try:
            cart_item = models.CartProduct.objects.get(carts_id=carts_id, products_id=products_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except models.CartProduct.DoesNotExist:
            self.instance = models.CartProduct.objects.create(
                carts_id=carts_id,
                **self.validated_data
            )
        return self.instance