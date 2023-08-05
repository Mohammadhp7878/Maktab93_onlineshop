from rest_framework import serializers
from products.serializers import SimpleProductSerializer
from . import models 


    
class CartProductSerializer(serializers.ModelSerializer):
        products = SimpleProductSerializer()
        total_price = serializers.SerializerMethodField()
        
        class Meta:
            model = models.CartProduct
            fields = ["id", "products", "quantity", "total_price"]

        def get_total_price(self, cart_products):
            return cart_products.quantity * cart_products.price


class CartSerializer(serializers.ModelSerializer):
    items = CartProductSerializer(many=True)
    
    class Meta:
        model = models.Cart
        fields = ["id", "items"]