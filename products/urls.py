from django.urls import path
from . import views


urlpatterns = [
    path('products_list/', views.ProductView.as_view(), name='products_list'),
    path('products_list_api/', views.ProductList.as_view(), name='products_list_api'),
]