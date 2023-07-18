from django.db import models
from core.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    parent = models.ForeignKey(to='Category', on_delete=models.SET_NULL)


class Product(BaseModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)
    description = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='media')
    max_order = models.PositiveSmallIntegerField()


# class Comment(BaseModel):
#     user = ...
#     product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
#     content = models.CharField(max_length=255)