from django.db import models
from core.models import BaseModel
from products.models import Product
from accounts.models import User

class Order(BaseModel):
    class OrderStatus(models.TextChoices):
        PENDING = ("P", "pending")
        DELIVERED = ("D", "delivered")
        SENDING = ("S", "sending")

    status = models.CharField(
        max_length=1, choices=OrderStatus.choices, default=OrderStatus.PENDING
    )
    deliver_time = models.TimeField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    detail = models.CharField(max_length=255)
    postal_code = models.CharField()

class ProductOrder(BaseModel):
    products = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    orders = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    

class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
        
        
class CartProduct(BaseModel):
    carts = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name='items')
    products = models.ForeignKey(to=Product, related_name='carts', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8 ,decimal_places=2)
    
    
    
    