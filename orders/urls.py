from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartPage.as_view(), name='cart_page')
]