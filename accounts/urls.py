from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfilePage.as_view(), name='profile'),
    path('login/', views.LoginPage.as_view(), name='login_page'),
    path('verify/', views.VerifyPage.as_view(), name='verify_page'),
    path('login_api/', views.LoginAPI.as_view(), name='login_api'),
    path('verify_api/', views.VerifyAPI.as_view(), name='verify_api'),
    path('logout/', views.LogOut.as_view(), name='logout')
]