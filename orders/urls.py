from django.urls import path, include
from . import views
from products.urls import router
from rest_framework_nested import routers


router.register('cart_api', views.CartViewSet, basename='cart')
cart_router = routers.NestedDefaultRouter(router, 'cart_api', lookup='cart')
cart_router.register('cart_products', views.CartProductsViewSet, basename='cart_product')


urlpatterns = [
    path('cart/', views.CartPage.as_view(), name='cart_page'),
    path('', include(router.urls)),
    path('', include(cart_router.urls)),
    
]