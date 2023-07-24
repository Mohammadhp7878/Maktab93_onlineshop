from django.db import models
from core.models import BaseModel
from accounts.models import User


class Category(BaseModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.CharField(max_length=255)
    parent = models.ForeignKey(to="Category", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"


class Gallery(BaseModel):
    image_url = models.ImageField(upload_to='media/')
    alt = models.CharField(max_length=250)
class Product(BaseModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)
    slug = models.SlugField()
    description = models.CharField(max_length=255)
    inventory = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    images = models.ForeignKey(to=Gallery, on_delete=models.SET_NULL, null=True)
    max_order = models.PositiveSmallIntegerField()


class Brand(BaseModel):
    brand_name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to="media/")
    products = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=True)


class Comment(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
