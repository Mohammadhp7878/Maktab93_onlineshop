from rest_framework import serializers
from products.serializers import SimpleProductSerializer
from . import models 


    
class CartProductSerializer(serializers.ModelSerializer):
        products = SimpleProductSerializer()
        item_total_price = serializers.SerializerMethodField()
        
        class Meta:
            model = models.CartProduct
            fields = ["id", "products", "quantity", "item_total_price"]

        def get_item_total_price(self, cart_products:models.CartProduct):
            if cart_products.products.discount:
                return cart_products.quantity * cart_products.products.discount_to_price
            return cart_products.quantity * cart_products.products.price


class CartSerializer(serializers.ModelSerializer):
    cartproducts = CartProductSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = models.Cart
        fields = ["id", "cartproducts", "total_price"]
        
    def get_total_price(self, cart:models.Cart):
        return sum([item.quantity * item.products.price if
                not item.products.discount else item.quantity * item.products.discount_to_price
                for item in cart.cartproducts.all()])