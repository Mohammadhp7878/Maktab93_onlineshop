from django.urls import path
from . import views

urlpatterns = [
    path('products_api', views.Home.as_view(), name='home_products'),
    path('', views.home, name='home')
]