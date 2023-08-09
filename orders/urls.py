from django.urls import path, include
from . import views
from products.urls import router


router.register('cart_api', views.CartViewSet, basename='cart')

urlpatterns = [
    path('cart/', views.CartPage.as_view(), name='cart_page'),
    path('', include(router.urls)),
    
]