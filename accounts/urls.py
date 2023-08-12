from django.urls import path
from . import views

urlpatterns = [
    path('login_api/', views.LoginAPI.as_view(), name='login'),
    # path('verify/', views.Verify.as_view(), name='verify_code'),
]