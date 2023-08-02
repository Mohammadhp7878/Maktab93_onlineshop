from django.shortcuts import render
from django.views import View
from rest_framework import generics, viewsets, permissions
from . import serializers
from . import models
from .permissions import IsCommentOwner
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework import filters

class ProductsPage(View):
    def get(self, request):
        return render(request, 'products.html')
    
    
class CategoryView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    
    
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name']
    ordering_fields = ['price', 'created_at']
    

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsCommentOwner]
    serializer_class = serializers.CommentSerializer  
    
    def get_queryset(self):
        #overwrite our get_queryset to retrieve objects for specific products
        return models.Comment.objects.filter(products=self.kwargs['product_pk'])
    
    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}