from django.shortcuts import render
from django.views import View
from rest_framework import generics, viewsets, permissions
from . import serializers
from . import models
from .permissions import IsCommentOwner


class ProductsPage(View):
    def get(self, request):
        return render(request, 'products.html')
    
    
class CategoryView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    
    
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsCommentOwner]
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer    