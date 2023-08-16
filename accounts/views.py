from django.shortcuts import render, redirect
from django.views import View
from django.core.cache import cache
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from hashlib import sha256
import random
from utilize import send_otp
from .models import User
from .serializers import PhoneSerializer, CodeSerializer

class LoginPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')


class VerifyPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'verify.html')


class LoginAPI(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            return Response({"message": "You are already logged in."}, status=400)
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data["phone_number"]
            code = str(random.randint(100000, 999999))
            hashed_code = sha256(code.encode()).hexdigest()
            # send_otp(phone_number, code)
            cache.set(phone_number, hashed_code)
            response = Response({"message": "OTP sent successfully"})
            response.set_cookie("phone_number", phone_number, 180)
            print(code)
            return response
        else:
            return Response(serializer.errors, status=400)


class VerifyAPI(APIView):
    def post(self, request):
        serializer = CodeSerializer(data=request.data)
        if serializer.is_valid():
            user_code = str(serializer.validated_data["code"])
            user_hashed_code = sha256(user_code.encode()).hexdigest()
            phone = request.COOKIES.get("phone_number")
            saved_code = cache.get(phone)
            if saved_code and saved_code == user_hashed_code:
                user_instance, created = User.objects.get_or_create(phone_number=phone)
                print(user_instance)
                login(request, user_instance)
                refresh_token = RefreshToken.for_user(user_instance)
                access_token = str(refresh_token.access_token)
                response = Response({"message": f"Welcome {phone}", "token": access_token})
                print(access_token)
                response.delete_cookie("phone_number")
                return response
            else:
                return Response({"message": "code is not valid"}, status=400)
        else:
            return Response(serializer.errors, status=400)
