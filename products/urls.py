from django.urls import path
from . import views


urlpatterns = [
    path('products_list/', views.ProductList.as_view(), name='products_list'),
    path('product/<int:pk>', views.SingleProduct.as_view(), name='single_product'),
]