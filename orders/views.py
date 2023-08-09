from django.shortcuts import render
from django.views import View
from .models import Cart
from .serializers import CartSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin

class CartPage(View):
    def get(self, request):
        return render(request, 'cart.html')


class CartViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Cart.objects.prefetch_related('cartproducts__products').all()
    serializer_class = CartSerializer 
    