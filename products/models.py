from django.db import models
from core.models import BaseModel
from accounts.models import User


class Category(BaseModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.TextField()
    parent = models.ForeignKey(
        to="self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        if self.parent:
            return f"{self.parent}-{self.name}"
        else:
            return self.name

    def get_children(self):
        children = [self]
        for child in self.children.all():
            children.extend(child.get_children())
        return children


class Gallery(BaseModel):
    image_url = models.ImageField(upload_to="media/")
    alt = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return f'{self.alt}'


class Brand(BaseModel):
    brand_name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to="media/")

    def __str__(self) -> str:
        return self.brand_name


class Product(BaseModel):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(to=Category, related_name="products")
    slug = models.SlugField()
    description = models.TextField()
    inventory = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    images = models.ForeignKey(to=Gallery, on_delete=models.SET_NULL, null=True)
    max_order = models.PositiveSmallIntegerField()
    brand = models.ForeignKey(
        to=Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )

    def __str__(self) -> str:
        return self.name


class Comment(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    products = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.id}'
