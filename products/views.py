from django.shortcuts import render
from django.views import View
from rest_framework import generics
from . import serializers
from . import models

class ProductView(View):
    def get(self, request):
        return render(request, 'products.html')


class ProductList(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer(instance=queryset)