from django.urls import path
from . import views


urlpatterns = [
    path('products_list/', views.ProductView.as_view(), name='products_list')
]