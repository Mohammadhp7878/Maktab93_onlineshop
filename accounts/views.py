from django.shortcuts import render, redirect
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from utilize import send_otp
from hashlib import sha256
import random
from .models import User
from .serializers import PhoneSerializer, CodeSerializer



class LoginAPI(APIView):
    def post(self, request):
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
                User.objects.get_or_create(phone_number=phone)
                response = Response({"message": f"Welcome {phone}"})
                response.delete_cookie("phone_number")
                return response
            else:
                return Response({"message": "code is not valid"}, status=400)
        else:
            return Response(serializer.errors, status=400)
