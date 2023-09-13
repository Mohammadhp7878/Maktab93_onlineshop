from django.views import View
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, permissions
from rest_framework import filters
from .permissions import IsCommentOwner
from .filters import ProductFilter
from .paginations import ProductsPagination
from . import serializers
from . import models


class ProductsPage(View):
    def get(self, request):
        return render(request, "products.html")


class CategoryView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.AllowAny]


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = ProductFilter
    pagination_class = ProductsPagination
    permission_classes = [permissions.AllowAny]
    search_fields = ["name"]
    ordering_fields = ["price", "created_at"]
    ordering = ["-created_at"]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsCommentOwner]

    def get_queryset(self):
        # overwrite our get_queryset to retrieve objects for specific products
        return models.Comment.objects.filter(products=self.kwargs["product_pk"])

    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}
