from django.db import models
from core.models import BaseModel 
from products.models import Product

class Order(BaseModel):
    class OrderStatus(models.TextChoices):
        PENDING = ('P', 'pending')
        DELIVERED = ('D', 'delivered')
        SENDING = ('S', 'sending')
    
    status = models.CharField(max_length=1, choices=OrderStatus.choices, 
                              default=OrderStatus.PENDING)
    deliver_time = models.TimeField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)