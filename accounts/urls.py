from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    # path('verify/', views.Verify.as_view(), name='verify_code'),
]