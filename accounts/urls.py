from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Register.as_view(), name='login'),
    path('verify/', views.Verify.as_view(), name='verify_code'),
]