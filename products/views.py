from django.shortcuts import render
from django.views import View
from rest_framework import generics
from . import serializers
from . import models


class ProductList(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return render(request, 'products.html', {'products': serializer.data})

class SingleProduct(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = 'pk'
    
class CategoryView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer