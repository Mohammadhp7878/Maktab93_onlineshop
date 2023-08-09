from django.shortcuts import render
from django.views import View
from .models import Cart, CartProduct
from .serializers import CartSerializer, CartProductSerializer, AddProductSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin

class CartPage(View):
    def get(self, request):
        return render(request, 'cart.html')


class CartViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Cart.objects.prefetch_related('cartproducts__products').all()
    serializer_class = CartSerializer 


class CartProductsViewSet(ModelViewSet):
    def get_queryset(self):
        return CartProduct.objects.filter(carts=self.kwargs['cart_pk']).select_related('products')
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddProductSerializer
        return CartProductSerializer
    
    def get_serializer_context(self):
        return {'cart_id':self.kwargs['cart_pk']}